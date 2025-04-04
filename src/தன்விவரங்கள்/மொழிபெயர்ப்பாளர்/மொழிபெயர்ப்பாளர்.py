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
    def __init__(தன், கோப்புரை: str, மொழிபெயர்ப்புகள்: Optional[dict[str]] = None):
        தன்.மொழிபெயர்ப்புகள் = மொழிபெயர்ப்புகள் or {}
        தன்.கோப்புரை = கோப்புரை

    @lru_cache()
    def _மொழிபெயர்ப்பு_கோப்பு_பெறு(தன், மொழி: str) -> dict:
        கோப்புரை = os.path.join(தன்.கோப்புரை, f"{மொழி}.json")
        if os.path.isfile(கோப்புரை):
            with open(கோப்புரை, encoding="utf8", mode="r") as கோ:
                மொழிபெயர்ப்புகள் = json.load(கோ)
                return மொழிபெயர்ப்புகள்
        return {}

    def __call__(தன், சாபி: str, மொழி: str) -> Optional[str]:
        சாபி_பகுதிகள் = சாபி.split(".")
        if மொழி in தன்.மொழிபெயர்ப்புகள்:
            for இ, சாபி_பகுதி in enumerate(சாபி_பகுதிகள்):
                அகராதி = தன்.மொழிபெயர்ப்புகள்[மொழி]
                try:
                    அகராதி = அகராதி[சாபி_பகுதி]
                    if இ == (len(சாபி_பகுதிகள்) -1):
                        return அகராதி
                except KeyError:
                    break

        கோப்பு_மொழிபெயர்ப்புகள் = தன்._மொழிபெயர்ப்பு_கோப்பு_பெறு(மொழி)
        அகராதி =  கோப்பு_மொழிபெயர்ப்புகள்
        for இ, சாபி_பகுதி in enumerate(சாபி_பகுதிகள்):
            try:
                அகராதி = அகராதி[சாபி_பகுதி]
                if இ == (len(சாபி_பகுதிகள்) - 1):
                    return அகராதி
            except KeyError:
                break


