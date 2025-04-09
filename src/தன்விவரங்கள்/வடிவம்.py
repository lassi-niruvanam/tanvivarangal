import uuid

from odfdo import Style


class வடிவம்(object):
    def __init__(தன்):
        தன்.பெயர் = str(uuid.uuid4())


class உரை_வடிவம்(வடிவம்):
    def __init__(தன், அளவு=12, சாய்வு=False, அடிக்கோடு=False, தடிமன்=False, குடும்பம்="Sans"):
        super().__init__()
        தன்.வடிவம் = {
            "சாய்வு": சாய்வு,
            "அடிக்கோடு": அடிக்கோடு,
            "தடிமன்": தடிமன்,
            "குடும்பம்": குடும்பம்,
            "அளவு": அளவு,
        }

    def சாய்வு(தன்):
        வடிவம் = தன்.வடிவம்.copy()
        வடிவம்["சாய்வு"] = not தன்.வடிவம்["சாய்வு"]
        return உரை_வடிவம்(**வடிவம்)

    def அடிக்கோடு(தன்):
        வடிவம் = தன்.வடிவம்.copy()
        வடிவம்["அடிக்கோடு"] = not தன்.வடிவம்["அடிக்கோடு"]
        return உரை_வடிவம்(**வடிவம்)

    def தடிமன்(தன்):
        வடிவம் = தன்.வடிவம்.copy()
        வடிவம்["தடிமன்"] = not தன்.வடிவம்["தடிமன்"]
        return உரை_வடிவம்(**வடிவம்)


class பத்தி_வடிவம்(வடிவம்):
    def __init__(தன், உள்தள்ளல்=0, ஒழுங்கு=None, கீழ்_ஓரம்=10, மேல்_ஓரம்=0):
        super().__init__()
        தன்.ஒழுங்கு = ஒழுங்கு
        தன்.உள்தள்ளல் = உள்தள்ளல்
        தன்.மேல்_ஓரம் = மேல்_ஓரம்
        தன்.கீழ்_ஓரம் = கீழ்_ஓரம்


class தேவையான_வடிவங்கள்(object):
    def __init__(தன்):
        தன்.வடிவங்கள் = set()

    def சேரு(தன், வடிவம்: வடிவம்):
        if isinstance(வடிவம், உரை_வடிவம்):
            தன்.வடிவங்கள்.add(Style(
                family="text",
                name=வடிவம்.பெயர்,
                display_name=வடிவம்.பெயர்,
                italic=வடிவம்.வடிவம்["சாய்வு"],
                underline=வடிவம்.வடிவம்["அடிக்கோடு"],
                bold=வடிவம்.வடிவம்["தடிமன்"],
                size=str(வடிவம்.வடிவம்["அளவு"]) + "pt",
                **{
                    "style:font-size-complex": str(வடிவம்.வடிவம்["அளவு"]) + "pt",
                    "style:font-size-asian": str(வடிவம்.வடிவம்["அளவு"]) + "pt",
                    "style:font-name": "DejaVu Sans" if வடிவம்.வடிவம்["குடும்பம்"] == "Sans" else "DejaVu Serif",
                    "style:font-name-asian": "DejaVu Sans" if வடிவம்.வடிவம்["குடும்பம்"] == "Sans" else "DejaVu Serif",
                    "style:font-name-complex": "DejaVu Sans" if வடிவம்.வடிவம்["குடும்பம்"] == "Sans" else "DejaVu Serif"

                }
            ))
        elif isinstance(வடிவம், பத்தி_வடிவம்):
            தன்.வடிவங்கள்.add(Style(
                family="paragraph",
                name=வடிவம்.பெயர்,
                display_name=வடிவம்.பெயர்,
                align="left" if வடிவம்.ஒழுங்கு == "இடது" else "right" if வடிவம்.ஒழுங்கு == "வலது" else "justify",
                margin_top=str(வடிவம்.மேல்_ஓரம்) + "cm",
                margin_bottom=str(வடிவம்.கீழ்_ஓரம்) + "cm",
                text_indent=str(வடிவம்.உள்தள்ளல்) + "cm",
                margin_left=str(-வடிவம்.உள்தள்ளல்) + "cm" if வடிவம்.உள்தள்ளல் < 0 else "0cm"
            ))
        else:
            raise TypeError(வடிவம்)
