from abc import ABC, abstractmethod
from typing import Iterator

from odfdo import Element

from ..மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்
from ..வடிவம் import தேவையான_வடிவங்கள்


class உருப்படி(ABC):
    def __init__(தன்):
        pass

    @abstractmethod
    def மொழியாக்கத்துக்காக(தன்) -> dict[str, dict[str, str]]:
        pass

    def உருப்படிகள்(தன்) -> Iterator["உருப்படி"]:
        yield from []

    def வெளியிடு(தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர், வடிவங்கள்: தேவையான_வடிவங்கள்) -> Iterator[Element]:
        for உரு in தன்.உருப்படிகள்():
            yield from உரு.வெளியிடு(மொழி=மொழி, மொழியாக்கம்=மொழியாக்கம், வடிவங்கள்=வடிவங்கள்)
