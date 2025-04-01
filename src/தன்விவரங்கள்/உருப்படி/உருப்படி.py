from abc import ABC, abstractmethod
from typing import Iterator, Iterable, List

from odfdo import Element

from ..மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்
from ..வடிவம் import தேவையான_வடிவங்கள்


class உருப்படி(ABC):
    def __init__(தன்):
        pass

    @abstractmethod
    def மொழியாக்கத்துக்காக(தன்) -> dict[str, dict[str, str]]:
        pass

    @abstractmethod
    def உருப்படிகள்(தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர்) -> Iterator["உருப்படி"]:
        pass

    def வெளியிடு(தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர், வடிவங்கள்: தேவையான_வடிவங்கள்) -> Iterable[Element]:
        வெளியீடு: List[Element] = []
        for உரு in தன்.உருப்படிகள்(மொழி=மொழி, மொழியாக்கம்=மொழியாக்கம்):
            if வெளியீடு is not None:
                வெளியீடு.extend(உரு.வெளியிடு(மொழி=மொழி, மொழியாக்கம்=மொழியாக்கம், வடிவங்கள்=வடிவங்கள்))

        if வெளியீடு is None:
            raise RuntimeError("உருப்படிகள் கிடைக்கவில்லை.")

        return வெளியீடு

