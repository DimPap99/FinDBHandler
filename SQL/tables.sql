
drop table IF EXISTS public.candle cascade;
CREATE TABLE IF NOT EXISTS public.candle
(
    OpenTime bigint,
    CloseTime bigint,
    OpenPrice double precision,
    ClosePrice double precision,
	High double precision,
    Low double precision,
	NumberOfTrades int,
	intervalId int,
	symbolId int,
    PRIMARY KEY (OpenTime, CloseTime, intervalId, symbolId)
);


drop table IF EXISTS public.interval cascade;
CREATE TABLE IF NOT EXISTS public.interval
(
    id serial,
    interval character varying unique,
	exchangeid integer,
    PRIMARY KEY (id)
);


drop table IF EXISTS public.symbol cascade;
CREATE TABLE IF NOT EXISTS public.symbol
(
    id serial,
    name character varying,
	exchangeid integer,
    PRIMARY KEY (name, exchangeid)
);