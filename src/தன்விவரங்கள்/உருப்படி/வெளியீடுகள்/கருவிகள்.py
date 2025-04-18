from nuchabäl import Nuchabäl

nchbl = Nuchabäl()


def சுத்தமான_உரை(உரை: str) -> str:
    return உரை.replace("\\&", "&").replace("{", "").replace("}", "")


