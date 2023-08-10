
from peewee import Database

class DB_Handler(object):
    
    def __init__(self, db:Database) -> None:
        self._db:Database = db
    