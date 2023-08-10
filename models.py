import sys
from sqlalchemy import Column, Float, BigInteger, SmallInteger, PrimaryKeyConstraint, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import BIGINT, INTEGER, SMALLINT, Integer, BLOB, String, Boolean, TIMESTAMP
from sqlalchemy.schema import UniqueConstraint
import os

script_dir = os.path.dirname(__file__)
DATABASE_NAME = "Algo_Trading"
Path_To_DB = os.path.join("/mnt/CryptoStorage","StockData.db")
CONNECTION_STRING = "sqlite:///"+ Path_To_DB #Use to connect to sqlite db --->Testing purposes
MYSQL_DATABASE_CONN_STRING = f"mysql+mysqlconnector://root:naruto123@localhost/{DATABASE_NAME}" #Use to connector straight to the database
MYSQL_SERVER_CONN_STRING = "mysql+mysqlconnector://root:naruto123@localhost" #Use to connect to the server
Base = declarative_base()
DB_EXISTS = False


def get_engine(create_db=False):
    return engine

class StockInfo(Base):
    intraday_multipliers = Column("intradayMultipliers", BLOB)


class DailyData(Base):
        self.turnover = turnover
        
class LastUpdate(Base):
    __tablename__ = "LastUpdate"
    timestamp = Column("timestamp", BigInteger, primary_key=True)
    name = Column("name", ForeignKey(StockInfo.name), primary_key=True)