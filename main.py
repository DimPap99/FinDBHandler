import csv
from models import Candle, Symbol, Interval, DATABASE
from DBClient import DBClient
from EnumTypes import DB_Type, Exchange
l = []
with open('C:\\Users\\torat\\Desktop\\CryptoData\\BTCEUR_1d.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(f'{", ".join(row)}')
        line_count += 1
        if line_count == 10:
            break
symbol = "BTCUSD"
interval = "1d"
handler = DBClient(DATABASE)

# handler.create_tables([Candle, Symbol, Interval])
# handler.upsertSymbol(symbol, str(Exchange.Binance))
# handler.upsertInterval(interval=interval)
