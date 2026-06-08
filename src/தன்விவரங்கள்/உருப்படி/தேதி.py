from datetime import datetime
from typing import Iterable, Optional

from babel import UnknownLocaleError, Locale
from babel.dates import format_date
from odfdo import Span

from .உருப்படி import உருப்படி
from .உரை import உரை
from .எண் import எண்
from .கருவிகள் import மொழி_சீயனைதி, உள்ளீடு_உரை
from .நிறுத்தற்குறிகள் import இடைவெளி, இணைப்புச்சிறுகோடு
from .மொழி_உரை import மொழிபெயர்க்கக்கூடிய_உரை
from ..மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்
from ..வடிவம் import உரை_வடிவம், தேவையான_வடிவங்கள்


class தேதி(உரை):
    def __init__(
        தன்,
        ஆண்டு: str | int | datetime,
        மாதம்: int = None,
        நாள்: int = None,
        வடிவம்: உரை_வடிவம் = None,
    ):
        if isinstance(ஆண்டு, datetime):
            தேதி_ = ஆண்டு
        else:
            தேதி_ = datetime(ஆண்டு, மாதம் or 1, நாள் or 1)
        super().__init__(உரை=str(தேதி_), வடிவம்=வடிவம்)
        தன்.ஆண்டு = ஆண்டு
        தன்.மாதம் = மாதம்
        தன்.நாள் = நாள்
        தன்.தேதி = தேதி_

    def வெளியிடு(
        தன், மொழி: str, மொழியாக்கம்: மொழிபெயர்ப்பாளர், வடிவங்கள்: தேவையான_வடிவங்கள்
    ) -> Iterable[Span]:
        வடிவங்கள்.சேரு(தன்.வடிவம், மொழி)
        try:
            மொழி_குறியீடு = மொழி_சீயனைதி(மொழி)
            if மொழி_குறியீடு:
                Locale.parse(மொழி_குறியீடு)
        except UnknownLocaleError:
            மொழி_குறியீடு = None

        try:
            if தன்.ஆண்டு == தன்.தேதி or தன்.நாள்:
                உரை_ = format_date(தன்.தேதி, locale=மொழி_குறியீடு)
            elif தன்.மாதம்:
                உரை_ = format_date(தன்.தேதி, "MMMM yyyy", locale=மொழி_குறியீடு)
            else:
                yield from எண்(தன்.ஆண்டு).வெளியிடு(மொழி, மொழியாக்கம், வடிவங்கள்)
                return
        except ValueError:
            உரை_ = தன்.உரை

        yield Span(உரை_, style=தன்.வடிவம்.பெயர்)


def தேதியாக(தேதி_: தேதி | datetime):
    return தேதி_ if isinstance(தேதி_, தேதி) else தேதி(தேதி_)


class தேதி_இடைவெளி(உருப்படி):
    def __init__(தன், ஆரம்ப_தேதி: தேதி, இறுதியான_தேதி: Optional[தேதி] = None):
        super().__init__()
        தன்.ஆரம்ப_தேதி = ஆரம்ப_தேதி
        தன்.இறுதியான_தேதி = இறுதியான_தேதி

    def உருப்படிகள்(தன்):
        yield from [தேதியாக(தன்.ஆரம்ப_தேதி), இடைவெளி(), இணைப்புச்சிறுகோடு(), இடைவெளி()]

        if தன்.ஆரம்ப_தேதி != தன்.இறுதியான_தேதி:
            yield (
                தேதியாக(தன்.இறுதியான_தேதி)
                if தன்.இறுதியான_தேதி
                else மொழிபெயர்க்கக்கூடிய_உரை(உள்ளீடு_உரை("தற்காலம்"), மூல்_சாபி="தேதிகள்")
            )
