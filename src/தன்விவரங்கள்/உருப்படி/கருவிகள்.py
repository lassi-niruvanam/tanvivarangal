from abc import abstractmethod
from typing import Iterable, Optional

from pyfranc import franc

from .வெளியீடுகள்.கருவிகள் import nchbl
from ..வடிவம் import உரை_வடிவம்


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


def மொழியின்_பெயர்(மொழி: str) -> str:
    try:
        வெளியீட்டின்_மொழி = nchbl.rubiChabäl(
            மொழி, 'iso'
        )

        return nchbl.runukChabäl(வெளியீட்டின்_மொழி or மொழி, None) or மொழி
    except ValueError:
        return மொழி


def மொழியைக்_கண்டுப்பிடி(உரை: str) -> str:
    ஃபிராங்க_ஊகி = franc.lang_detect(உரை)[0][0]
    return மொழியின்_பெயர்(ஃபிராங்க_ஊகி)


class உள்ளீடு_உரை(object):
    def __init__(தன், உரை: str, மூல்_மொழி: Optional[str]):
        super().__init__()
        தன்.உரை = உரை
        தன்.மூல்_மொழி = மூல்_மொழி or மொழியைக்_கண்டுப்பிடி(உரை)
