import warnings
from typing import Iterator

import bibtexparser

from .கட்டுரை import கட்டுரை
from .நூல் import நூல்
from .மாநாடு_கட்டுரை import மாநாடு_கட்டுரை
from ..உருப்படி import உருப்படி
from ..கருவிகள் import எழுத்தாளர்_வடிவம்


class வெளியீடுகள்(உருப்படி):

    def __init__(தன், பிப்தேக்ஸ்_கோப்பு: str, எழுத்தாளர்_வடிவூட்டி: எழுத்தாளர்_வடிவம் = None):
        super().__init__()
        தன்.எழுத்தாளர்_வடிவூட்டி = எழுத்தாளர்_வடிவூட்டி

        with open(பிப்தேக்ஸ்_கோப்பு) as f:
            தன்.பட்டியல் = bibtexparser.load(f)

    def உருப்படிகள்(தன்) -> Iterator["உருப்படி"]:
        for ப in தன்.பட்டியல்.entries:
            if உரு := தன்._உருப்படியை_உருவாக்கு(ப):
                yield உரு

    def மொழியாக்கத்துக்காக(தன்) -> dict[str, str]:
        return {}

    def _உருப்படியை_உருவாக்கு(தன், தகவல்கள்: dict[str, str]):
        வகை = தகவல்கள்["ENTRYTYPE"]
        if வகை == "article":
            return கட்டுரை(தகவல்கள், தன்.எழுத்தாளர்_வடிவூட்டி)
        elif வகை == "book":
            return நூல்(தகவல்கள், தன்.எழுத்தாளர்_வடிவூட்டி)
        elif வகை == "inproceedings":
            return மாநாடு_கட்டுரை(தகவல்கள், தன்.எழுத்தாளர்_வடிவூட்டி)
        else:
            warnings.warn("தெரியாத வெளியீடு வகை " + வகை)
