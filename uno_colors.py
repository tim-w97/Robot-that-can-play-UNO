from enum import Enum
from colormath.color_objects import sRGBColor


# format is RGB
class UnoColors(Enum):
    RED = sRGBColor(198, 42,	53)
    YELLOW = sRGBColor(239, 211, 46)
    GREEN = sRGBColor(88, 166, 54)
    BLUE = sRGBColor(3, 93, 172)
