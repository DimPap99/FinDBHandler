
CREATE OR REPLACE FUNCTION public.candle_partition_creation(symbolId INT, intervalId INT)
RETURNS VOID AS $$
DECLARE
    q TEXT = 'public.candle_' || symbolId || '_' || intervalId;
BEGIN
    
    EXECUTE 'CREATE TABLE IF NOT EXISTS ' || q || ' (LIKE public.candle INCLUDING ALL)';
     IF NOT EXISTS (
            SELECT 1
            FROM pg_inherits
            WHERE inhrelid = q::regclass AND inhparent = 'public.candle'::regclass
        ) THEN
	EXECUTE 'ALTER TABLE ' || q || ' INHERIT public.candle';
	
    EXECUTE 'CREATE INDEX IF NOT EXISTS idx_candle_symbol' || symbolId || ' ON ' || q || ' (SymbolId)';
    EXECUTE 'CREATE INDEX IF NOT EXISTS idx_candle_interval' || intervalId || ' ON ' || q || ' (IntervalId)';
    END IF;

END;
$$
LANGUAGE plpgsql;


create or replace function public.candle_partition_function()
returns trigger as $$
begin
    execute 'insert into public.candle_'
        ||  NEW.SymbolId || '_' || NEW.IntervalId
        || ' values ($1,$2,$3,$4,$5,$6,$7,$8,$9 )' 
    
    using NEW.OpenTime,NEW.CloseTime,NEW.OpenPrice, NEW.ClosePrice,   NEW.High,NEW.Low,NEW.NumberOfTrades, NEW.IntervalId,NEW.SymbolId
   
    return null;
end;
$$
language plpgsql;

-- drop trigger public_candle_partition_trigger;
create or replace trigger public_candle_partition_trigger
    before insert
    on public.candle
    for each row
    execute procedure public.candle_partition_function() ;


    