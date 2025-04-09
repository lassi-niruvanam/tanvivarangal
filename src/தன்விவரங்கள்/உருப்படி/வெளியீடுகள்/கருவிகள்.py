from nuchabäl import Nuchabäl
from pyfranc import franc

nchbl = Nuchabäl()


def சுத்தமான_உரை(உரை: str) -> str:
    return உரை.replace("\\&", "&").replace("{", "").replace("}", "")


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
