from DBEnums import DB_Type
from peewee import SqliteDatabase, MySQLDatabase, PostgresqlDatabase
class DB_Helper:

    @classmethod
    def get_database(cls, db_type:DB_Type, db_name:str, **kwargs):
        try:
            
            if db_type == DB_Type.SQLite:
                return SqliteDatabase(db_name, kwargs=kwargs)
            elif db_type == DB_Type.MySQL:
                return MySQLDatabase(db_name, kwargs=kwargs)
            elif db_type == DB_Type.PostgreSQL:
                return PostgresqlDatabase(db_name, kwargs=kwargs)
            else:
                raise ValueError("The db_Type that was provided is not supported...")
        except ValueError as ex:
            print(ex)
        except Exception as ex:
            print(f"An exception occured: {ex}")