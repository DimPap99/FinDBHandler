from DB_Client import DB_Client
from EnumTypes import DB_Type


class DB_Handler(object):
    
    def __init__(self, clients:[DB_Client], dbType, asset_info_client=None) -> None:
        self.clients = clients
        self.dbType = dbType
        if self.dbType == DB_Type.SQLite:
            self.asset_info_client = asset_info_client
