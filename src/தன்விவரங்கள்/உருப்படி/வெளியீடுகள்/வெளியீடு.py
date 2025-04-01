from abc import abstractmethod

from nuchabäl import Wuj

from ..உருப்படி import உருப்படி
from ...மொழிபெயர்ப்பாளர்.மொழிபெயர்ப்பாளர் import மொழிபெயர்ப்பாளர்

wuj = Wuj()


class வெளியீடு(உருப்படி):
    @abstractmethod
    def வடிவூட்டம்(தன், மொழி: str, தகவல்கள்: dict[str, str], மொழிப்பெயர்பாளர்: மொழிபெயர்ப்பாளர்) -> str:
        pass

