from typing import Iterable

from odfdo import Span
from எண்ணிக்கை import உரைக்கு
from .உரை import உரை
from .வெளியீடுகள்.கருவிகள் import wuj
from ..வடிவம் import உரை_வடிவம், தேவையான_வடிவங்கள்
from ..மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்


class எண்(உரை):
    def __init__(தன், எண்: int | float, வடிவம்: உரை_வடிவம் = None):
        super().__init__(உரை=str(எண்), வடிவம்=வடிவம்)
        தன்.எண் = எண்

    def வெளியிடு(தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர், வடிவங்கள்: தேவையான_வடிவங்கள்) -> Iterable[Span]:
        வடிவங்கள்.சேரு(தன்.வடிவம்)
        try:
            உரை = உரைக்கு(தன்.உரை, மொழி=wuj.ruchabäl(மொழி))
        except ValueError:
            உரை = தன்.உரை
        yield Span(உரை, style=தன்.வடிவம்.பெயர்)
