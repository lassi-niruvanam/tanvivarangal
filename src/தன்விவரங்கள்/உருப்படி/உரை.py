from typing import Iterator, Iterable

from odfdo import Element, Span

from .உருப்படி import உருப்படி
from ..வடிவம் import உரை_வடிவம், தேவையான_வடிவங்கள்
from ..மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்


class உரை(உருப்படி):
    def __init__(தன், உரை: str, வடிவம்: "உரை_வடிவம்" = None):
        super().__init__()
        தன்.உரை = உரை
        தன்.வடிவம் = வடிவம் or உரை_வடிவம்()

    def வெளியிடு(தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர், வடிவங்கள்: தேவையான_வடிவங்கள்) -> Iterable[Element]:
        வடிவங்கள்.சேரு(தன்.வடிவம்)

        yield Span(தன்.உரை, style=தன்.வடிவம்.பெயர்)
