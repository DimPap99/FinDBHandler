
from peewee import Database

from EnumTypes import DB_Type
from peewee import SqliteDatabase, MySQLDatabase, PostgresqlDatabase
from models import Symbol, Interval, Candle, AssetInfo

class DB_Client(object):
    
    def __init__(self, db:Database, dbType:DB_Type, isAssetInfo=False, asset_n=None) -> None:
        self._db:Database = db
        tables = []
        if dbType == DB_Type.SQLite:
            if isAssetInfo:
                tables.append(AssetInfo)
            else:
                tables.extend([Candle, Symbol, Interval])
                self.asset_name = asset_n
        self.create_tables(tables)
    
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