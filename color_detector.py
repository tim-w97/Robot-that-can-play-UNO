from uno_colors import UnoColors

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000


def determine_color(color_bgr):
    color_to_compare = sRGBColor(color_bgr[2], color_bgr[1], color_bgr[0])

    min_diff = None
    color = None

    for uno_color in UnoColors:
        # Convert from RGB to Lab Color Space
        color1_lab = convert_color(color_to_compare, LabColor)
        color2_lab = convert_color(uno_color.value, LabColor)

        # Find the color difference
        diff = delta_e_cie2000(color1_lab, color2_lab)

        if min_diff is None or diff < min_diff:
            min_diff = diff
            color = uno_color

    return color
