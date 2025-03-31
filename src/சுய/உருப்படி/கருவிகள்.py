from abc import abstractmethod
from typing import Iterable

from சுய.வடிவம் import உரை_வடிவம்


class எழுத்தாளர்_வடிவம்(object):
    @abstractmethod
    def வடிவம்(தன், எழுத்தாளர்: str) -> உரை_வடிவம்:
        pass


class நான்_தடிமன்_எழுத்தாளர்_வடிவம்(எழுத்தாளர்_வடிவம்):

    def __init__(தன், என்_பெயர்கள்: Iterable[str]):
        தன்.என்_பெயர்கள் = என்_பெயர்கள்

    def வடிவம்(தன், எழுத்தாளர்):
        if எழுத்தாளர் in தன்.என்_பெயர்கள்:
            return உரை_வடிவம்(தடிமன்=True)
