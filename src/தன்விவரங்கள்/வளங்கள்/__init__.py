import json
from functools import lru_cache
from importlib import resources
from json import JSONDecodeError

கோப்புரை = resources.files("தன்விவரங்கள்.வளங்கள்.மொழிபெயர்ப்புகள்")


@lru_cache()
def பொது_மொழிபெயர்ப்புகளைப்_பேறு(மொழி: str) -> dict[str, str | dict] | None:
    கோப்பு = கோப்புரை.joinpath(f"{மொழி}.json")
    try:
        with open(கோப்பு, encoding="utf8", mode="r") as w:
            return {"பொது": json.load(w)}
    except (FileNotFoundError, JSONDecodeError):
        return None
