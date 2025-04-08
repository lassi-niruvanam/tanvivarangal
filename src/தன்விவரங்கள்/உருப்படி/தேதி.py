from .உரை import உரை
from .எண் import எண்
from ..வடிவம் import உரை_வடிவம்


class தேதி(எண்):
    def __init__(தன், ஆண்டு: int, வடிவம்: "உரை_வடிவம்" = None):
        # செய்யவும்
        super().__init__(எண்=ஆண்டு, வடிவம்=வடிவம்)
