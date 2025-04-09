from nuchabäl import Nuchabäl
from pyfranc import franc

nchbl = Nuchabäl()


def சுத்தமான_உரை(உரை: str) -> str:
    return உரை.replace("\\&", "&").replace("{", "").replace("}", "")


def மொழியைக்_கண்டுப்பிடி(உரை: str) -> str:
    ஃபிராங்க_ஊகி = franc.lang_detect(உரை)[0][0]
    try:
        வெளியீட்டின்_மொழி = nchbl.rubiChabäl(
            ஃபிராங்க_ஊகி, 'iso'
        )

        return nchbl.runukChabäl(வெளியீட்டின்_மொழி, None) or ஃபிராங்க_ஊகி
    except ValueError:
        return ஃபிராங்க_ஊகி
