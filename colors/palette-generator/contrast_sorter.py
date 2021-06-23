import random
import wcag_contrast_ratio as contrast
from colour import Color
import get_complement
WCAG_THRESHOLD = 3.25


def triadic_scheme(hexcode):
    """
    """
    colour_obj = Color(hexcode)
    (hue, saturation, lightness) = colour_obj.hsl
    rotated = rotate_120(hue)
    
    sibling1 = (
        rotated[0],
        saturation,
        lightness
    )
    sibling2 = (
        rotated[1],
        saturation,
        lightness
    )
    return [Color(hsl=sibling1).hex_l, Color(hsl=sibling2).hex_l]


def rotate_120(hue):
    rotated1 = hue - .333333333333333333333333333333333
    rotated2 = hue + .333333333333333333333333333333333
    
    for rotated in [rotated1, rotated2]:
        if rotated > 1.0:
            rotated -= 1.0
        elif rotated < 0.0:
            rotated += 1.0

    return [rotated1, rotated2]



def highest_contrast_pair(hex_list):
    """
    Get highest possible contrast pair between any two hexcodes in list.

    Args:
        hex_list (list) : list of hexcodes

    Returns:
        list:
            tuple: (rgb1, rgb2)
            tuple: (hex1, hex2)
        float: contrast ratio between the chosen pair
    """

    rgbs = {}
    # Make rgb conversion dict
    for color in hex_list:
        colour_obj = Color(color)
        validated = floor_rgb(colour_obj)
        rgb_tuple = validated.rgb
        rgbs[color] = rgb_tuple

    max_contrast = 0
    max_contrast_pair = []
    
    for hexcode, rgb_val in rgbs.items():
        for hex_complement, complement in rgbs.items():
            ratio = contrast.rgb(rgb_val, complement)
            if ratio > max_contrast:
                max_contrast = ratio
                max_contrast_pair = [
                    (rgb_val, complement),
                    (hexcode, hex_complement)
                ]

    return max_contrast_pair, max_contrast


def floor_rgb(colour):
    """
    Validates the rgb values in a color object are in range [0,1.0] 
    
    Args:
       colour (obj) : colour object
    
    Returns:
        obj : validated colour object
    """
    validated = [1.0]*3
    for index, rgb_value in enumerate(colour.rgb):
        if rgb_value < 0:
            validated[index] = 0.00001
        elif rgb_value < 1.0:
            validated[index] = rgb_value
   
    ret = Color(
        rgb=tuple(validated)
    )

    return ret


def increase_contrast(primary_color, secondary_color):
    """
    """

    # Determine the bright color and the dark color
    if primary_color.luminance > secondary_color.luminance:
        bright = [primary_color, secondary_color]
    else:
        bright = [secondary_color, primary_color]
    
    # Adjust luminance and saturation until meets WCAG_THRESHOLD
    while contrast.rgb(primary_color.rgb, secondary_color.rgb) < WCAG_THRESHOLD:
        
        # Priortize dimming dark color and brightening light color
        if bright[0].luminance < .998:
            bright[0].luminance += .000025
        if bright[1].luminance > .00015:
            bright[1].luminance -= .000025

        # Increase bright color saturation and vice-versa
        if bright[0].luminance >= .95 and bright[1].luminance <= .05:
            if bright[0].saturation < .99:
                bright[0].saturation += .0001
            if bright[1].saturation > .02:
                bright[1].saturation -= .000005
            if bright[0].saturation >= .99 and bright[1].saturation <= .02:
                break


def map_deepin_theme(background, foreground):
    """
    """ 
    theme = {
        "color_1=" : False,
        "color_2=" : False,
        "color_3=" : False,
        "color_4=" : False,
        "color_5=" : False,
        "color_6=" : False,
        "color_7=" : False,
        "color_8=" : False,
        "color_9=" : False,
        "color_10=" : False,
        "color_11=" : False,
        "color_12=" : False,
        "color_13=" : False,
        "color_14=" : False,
        "color_15=" : False,
        "color_16=" : False,
        "background=" : background.hex_l,
        "foreground=" : foreground.hex_l,
        "tab=" : False,
        "style=" : "dark" if background.luminance < .5 else "light"
    }
    return theme


def rank_contrast(color_list, background_color):
    """
    Rank secondary colors on basis of contrast with bg color. Dict for each theme.
    
    Args:
        color_list (list) : list of hexcode strings
        background_color (obj) : colour object of background

    Returns:
        dict: 
            contrast ratio : hexcode
    """    
    contrast_with_bg = {}
    for hexcode in color_list:
        colour_obj = Color(hexcode)
        rgb_adjusted = [1.0]*3
        for index, rgb_val in enumerate(colour_obj.rgb):
            if rgb_val <= 1.0 and rgb_val >= 0:
                rgb_adjusted[index] = rgb_val
        
        rank = contrast.rgb(background_color.rgb, tuple(rgb_adjusted))
        contrast_with_bg[rank] = hexcode

    return contrast_with_bg


def complementary_color(hexcode):
    """
    """
    colour_obj = Color(hexcode)
    complement_rgb = get_complement.complement(
        *colour_obj.rgb
    )
    colour_obj = Color(rgb=complement_rgb)
    return colour_obj.hex_l


def fill_theme(theme):
    """

    Args:
        theme (dict) : color_# : hexcode
    """

    non_accents = ["style="]
    accents = []
    for name, code in theme.items():
        if code:
            if "#" in code:
                if name not in non_accents:
                    accents.append(code)    

    # Fill with tradic rotated complements
    complement_colors = []
    for color_tier in ["background=", "color_1=", "color_2=", "color_3="]:
        if theme[color_tier]:
            complement_colors.append(
                complementary_color(
                    theme[color_tier]
                )
            )

            bg_triadic = triadic_scheme(
                theme[color_tier]
            )
            for _ in bg_triadic: complement_colors.append(_)

    mono_partners = []    
    for hexcode in accents:
        color_obj = Color(hexcode)
        if color_obj.saturation < .5:
            color_obj.saturation += .2
        else:
            color_obj.saturation -= .2
        mono_partners.append(
            color_obj.hex_l
        )
    
    accents += complement_colors + mono_partners
    accents *= 30

    ret = {}
    for index, (slot, hexcode) in enumerate(theme.items()):
        if not hexcode:
            ret[slot] = complementary_color(accents[index])
        else:
            ret[slot] = hexcode

    return ret


def contrast_check(color_list):
    """
    Accpets list of hexcodes and creates 2 deepin-terminal themes.
    Finds pair of colors that have highest contraste ratio between them and creates
    two themes by using those two for foreground/background and background/foreground,
    respectively. Then fills in rest of hexcodes as the text-highlighting
    colors, ranking them in order of contrast with the bg color. Then fills in any extra
    color slots by slightly changing saturation and luminance of the highest contrast
    text colors. 

    Args:
        color_list (list) : a list of hexcode strings (starting with '#')
    
    Returns:
        list:
            dict :
                colors: hexcodes
            dict :
                colors: hexcodes

    WCAG:
        WCAG 2.0 level AA requires a contrast ratio of at least 4.5:1
        for normal text and 3:1 for large text. 
        WCAG 2.1 requires a contrast ratio of at least 3:1 for graphics
        and user interface components (such as form input borders). 
        WCAG Level AAA requires a contrast ratio of at least 7:1 for 
        normal text and 4.5:1 for large text.

    """

    # Get highest contrast pair and the associated contrast ratio between them
    bg_fg_pair = highest_contrast_pair(color_list)
    max_contrast = bg_fg_pair[1]
    max_contrast_pair = bg_fg_pair[0]

    # Convert max-contrast pair to validated colour objects
    primary_color = floor_rgb(
        Color(
            rgb=max_contrast_pair[0][0]
        )
    )
    secondary_color = floor_rgb(
        Color(
            rgb=max_contrast_pair[0][1]
        )
    )
    
    # Contrsat ratio validation.
    increase_contrast(primary_color, secondary_color)

    # Other passed colors that aren't forground or background colors. 
    accent_colors = []
    for hexcode in color_list:
        if hexcode not in max_contrast_pair[1]:
            accent_colors.append(hexcode)

    # Create 2 themes with foreground/background alternating values 
    theme1 = map_deepin_theme(primary_color, secondary_color)
    theme2 = map_deepin_theme(secondary_color, primary_color)

    # Fill in themes' accent colors values in order of contrast with bg
    contrast_with_bg = [
        rank_contrast(accent_colors, primary_color),
        rank_contrast(accent_colors, secondary_color)
    ]
    for contrast_lvl, color_num in zip(reversed(sorted(contrast_with_bg[0])), theme1.keys()):
        theme1[color_num] = contrast_with_bg[0][contrast_lvl]    
    for contrast_lvl, color_num in zip(reversed(sorted(contrast_with_bg[1])), theme2.keys()):
        theme2[color_num] = contrast_with_bg[1][contrast_lvl]

    # Fill empty slots (hex list not long enough for deepin scheme) with complements of existing colors
    ret = [
        fill_theme(theme1),
        fill_theme(theme2)
    ]

    return ret