from typing import Iterable

from odfdo import Element, Link

from .உரை import உரை
from ..மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்
from ..வடிவூட்டு import தேவையான_வடிவங்கள்


class இணைப்பு(உரை):
    def __init__(தன், உரை: str, இணைப்பு: str, வடிவூட்டு: "உரை_வடிவூட்டு" = None):
        super().__init__(உரை, வடிவூட்டு)
        தன்.இணைப்பு = இணைப்பு

    def வெளியிடு(தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர், வடிவங்கள்: தேவையான_வடிவங்கள்) -> Iterable[Element]:
        வடிவங்கள்.சேரு(தன்.வடிவூட்டு)

        yield Link(url=தன்.இணைப்பு, text=தன்.உரை, style=தன்.வடிவூட்டு.பெயர்)
