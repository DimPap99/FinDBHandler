
from peewee import Database

from EnumTypes import DB_Type
from peewee import SqliteDatabase, MySQLDatabase, PostgresqlDatabase
from models import Symbol, Interval, Candle

class DB_Handler(object):
    
    def __init__(self, db:Database) -> None:
        self._db:Database = db
    

    def create_tables(self, list):
        with self._db.connection_context():
            self._db.create_tables(list)

    def upsertInterval(self, interval:str):
        with self._db.connection_context():
            Interval.insert(interval=interval).on_conflict("ignore").execute()

    def upsertSymbol(self, name, eId):
        with self._db.connection_context():
            Symbol.insert(Name=name, ExchangeId=eId).on_conflict("ignore").execute()


    def upsert_many(self, data):
        pass