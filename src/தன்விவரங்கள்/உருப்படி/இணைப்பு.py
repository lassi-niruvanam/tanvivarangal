from typing import Iterable

from odfdo import Element, Link

from .உரை import உரை
from ..மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்
from ..வடிவம் import தேவையான_வடிவங்கள், உரை_வடிவம்


class இணைப்பு(உரை):
    def __init__(தன், உரை_: str, இணைப்பு: str = None, வடிவம்: உரை_வடிவம் = None):
        super().__init__(உரை_, வடிவம்)
        தன்.இணைப்பு = இணைப்பு or உரை_

    def வெளியிடு(
        தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர், வடிவங்கள்: தேவையான_வடிவங்கள்
    ) -> Iterable[Element]:
        வடிவங்கள்.சேரு(தன்.வடிவம், மொழி)

        yield Link(url=தன்.இணைப்பு, text=தன்.உரை, style=தன்.வடிவம்.பெயர்)
