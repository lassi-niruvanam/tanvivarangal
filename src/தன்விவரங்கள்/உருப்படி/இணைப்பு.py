from typing import Iterable

from odfdo import Element, Link

from .உருப்படி import உருப்படி
from .உரை import உரை
from ..மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்
from ..வடிவம் import தேவையான_வடிவங்கள்


class இணைப்பு(உரை):
    def __init__(தன், உரை: str, இணைப்பு: str, வடிவம்: "உரை_வடிவம்" = None):
        super().__init__(உரை, வடிவம்)
        தன்.இணைப்பு = இணைப்பு

    def வெளியிடு(தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர், வடிவங்கள்: தேவையான_வடிவங்கள்) -> Iterable[Element]:
        வடிவங்கள்.சேரு(தன்.வடிவம்)

        yield Link(url=தன்.இணைப்பு, text=தன்.உரை, style=தன்.வடிவம்.பெயர்)
