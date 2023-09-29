from enum import Enum

class DB_Type(Enum):
    SQLite = 1,
    MySQL = 2,
    PostgreSQL = 3

class Exchange(Enum):
    Binance = 1,
    Kraken = 2,#not implemented yet
    Other = 3 #not implemented yet

class FinancialDataTypes(Enum):
    Candles = 0,
    Ticks = 1,
    Sentiment = 2,
    Transactions = 3,
    StreamEvents = 4
