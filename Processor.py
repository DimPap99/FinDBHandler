from abc import ABC, abstractmethod
#Open time, Open, High, Low, Close, Volume,	Close time, Number Of Trades

class Processor(ABC):

    @abstractmethod
    def process_candles(self, data):
        pass


class BinanceProcessor(Processor):

    def __init__(self) -> None:
        super().__init__()
    
    def process_candles(self, data)
        