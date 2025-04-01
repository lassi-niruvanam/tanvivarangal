from typing import Iterator

from .வெளியீடு import வெளியீடு
from ...மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்
from ...வடிவம் import தேவையான_வடிவங்கள்


class மாநாடு_கட்டுரை(வெளியீடு):

    def __init__(தன், தகவல்கள்: dict[str, str]):
        super().__init__()

    def மொழியாக்கத்துக்காக(தன்) -> dict[str, dict[str, str]]:
        return {}
    def உருப்படிகள்(தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர், வடிவங்கள்: தேவையான_வடிவங்கள்) -> Iterator[
        "உருப்படி"]:
        pass
