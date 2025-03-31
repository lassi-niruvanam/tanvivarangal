import json
import os
from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Optional


class மொழிபெயர்ப்பாளர்(ABC):
    @abstractmethod
    def __call__(தன், சாபி: str, மொழி: str) -> Optional[str]:
        pass

class ஜெஸான்_மொழிபெயர்ப்பாளர்(மொழிபெயர்ப்பாளர்):
    def __init__(தன், கோப்புரை: str, மொழிபெயர்ப்புகள்: Optional[dict[str, dict[str, str]]] = None):
        தன்.மொழிபெயர்ப்புகள் = மொழிபெயர்ப்புகள் or {}
        தன்.கோப்புரை = கோப்புரை

    @lru_cache()
    def _மொழிபெயர்ப்பு_கோப்பு_பெறு(தன், மொழி: str) -> dict[str, str]:
        கோப்புரை = os.path.join(தன்.கோப்புரை, f"{மொழி}.json")
        if os.path.isfile(கோப்புரை):
            with open(கோப்புரை, encoding="utf8", mode="r") as கோ:
                மொழிபெயர்ப்புகள் = json.load(கோ)
                return மொழிபெயர்ப்புகள்
        return {}

    def __call__(தன், சாபி: str, மொழி: str) -> Optional[str]:
        if மொழி in தன்.மொழிபெயர்ப்புகள்:
            if சாபி in தன்.மொழிபெயர்ப்புகள்[மொழி]:
                return தன்.மொழிபெயர்ப்புகள்[மொழி][சாபி]

        கோப்பு_மொழிபெயர்ப்புகள் = தன்._மொழிபெயர்ப்பு_கோப்பு_பெறு(மொழி)
        if சாபி in கோப்பு_மொழிபெயர்ப்புகள்:
            return கோப்பு_மொழிபெயர்ப்புகள்[சாபி]


