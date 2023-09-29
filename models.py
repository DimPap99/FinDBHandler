import sys
from playhouse.shortcuts import ThreadSafeDatabaseMetadata
from peewee import *
from EnumTypes import DB_Type

    
def get_database(db_type:DB_Type, db_name:str, **kwargs):
    try:
        user= None if 'user' not in kwargs else kwargs['user']
        password = None if 'password' not in kwargs else kwargs['password']
        host=None if 'host' not in kwargs else kwargs['host']
        port=None if 'port' not in kwargs else kwargs['port']
        pragmas = None if 'pragmas' not in kwargs else kwargs['pragmas']
        if db_type == DB_Type.SQLite:
            return SqliteDatabase(db_name, kwargs)
        elif db_type == DB_Type.MySQL:
            return MySQLDatabase(db_name, kwargs)
        elif db_type == DB_Type.PostgreSQL:
            print(kwargs)
            return PostgresqlDatabase(db_name, user=user, password=password, host=host, port=port)
        else:
            raise ValueError("The db_Type that was provided is not supported...")
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(f"An exception occured: {ex}")

    
#DATABASE = DB_Handler.get_database(DB_Type.post, "C:\\Users\\torat\\Projects\\dbs\\findb.db" )
DATABASE = get_database(DB_Type.PostgreSQL, "CryptoData", user='postgres', password='4655', host='localhost', port=5432  )

class BaseModel(Model):
    class Meta:
        # Instruct peewee to use our thread-safe metadata implementation.
        model_metadata_class = ThreadSafeDatabaseMetadata
        database = DATABASE

class Symbol(BaseModel):
    id = AutoField()
    Name = TextField(null=False, unique=True, column_name="name")
    ExchangeId = IntegerField(null=False, unique=True, column_name="exchangeid")
    class Meta:
        table_name = 'symbol'

class Interval(BaseModel):
    id = AutoField()
    interval = TextField(null=False, unique=True, column_name="interval")
    class Meta:
        table_name = 'interval'

class Candle(BaseModel):

    open_time = BigIntegerField(null=False, column_name="OpenTime")
    close_time = BigIntegerField(null=False, column_name="CloseTime")
    open_price = DoubleField(null=False, column_name="OpenPrice")
    close_price = DoubleField(null=False, column_name="ClosePrice")
    high = DoubleField(null=False, column_name="High")
    low = DoubleField(null=False, column_name="Low")
    number_of_trades = IntegerField(null=True, column_name="NumberOfTrades")
    interval_id = IntegerField(null=False, column_name="IntervalId")
    symbol_id = IntegerField(null=False, column_name="SymbolId")

    class Meta:
        table_name = 'candle'
        primary_key = CompositeKey('open_time', 'close_time', 'symbol_id', 'interval_id')
        