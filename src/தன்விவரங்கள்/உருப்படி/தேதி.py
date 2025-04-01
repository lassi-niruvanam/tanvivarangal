from .உரை import உரை
from ..வடிவம் import உரை_வடிவம்


class தேதி(உரை):
    def __init__(தன், ஆண்டு: int, வடிவம்: "உரை_வடிவம்" = None):
        # செய்யவும்
        super().__init__(உரை=str(ஆண்டு), வடிவம்=வடிவம்)
