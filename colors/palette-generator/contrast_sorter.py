import random


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
    import wcag_contrast_ratio as contrast
    from colour import Color
    WCAG_THRESHOLD = 3.85

    ret = {}
    # Make rgb conversion dict
    for color in color_list:
        r = Color(color)
        r = r.rgb
        ret[color] = r

    # Find highest contrast pair
    max_contrast = 0
    max_contrast_pair = []

    for hex, rgba in ret.items():
        

        for hex_sibling, sibling in ret.items():
            try:
                x = contrast.rgb(rgba, sibling)
            except:
                try:
                    x = contrast.rgb((1.0,.03,.3), sibling)
                except:
                    x = 1.0

            if x > max_contrast:
                max_contrast = x
                max_contrast_pair = [
                    (rgba, sibling),
                    (hex, hex_sibling)
                ]

    color1 = Color(
        rgb=max_contrast_pair[0][0]
    )
    color2 = Color(
        rgb=max_contrast_pair[0][1]
    )


    # Validate no rgb value > 1.0
    color3 = [1.0]*3
    color4 = [1.0]*3
    for index, _ in enumerate(color1.rgb):
        if _ < 1.0:
            color3[index] = _
    for index, _ in enumerate(color2.rgb):
        if _ < 1.0:
            color4[index] = _
   
    color3 = tuple(color3)
    color4 = tuple(color4)
    color_one = Color(
        rgb=color3
    )
    color_two = Color(
        rgb=color4
    )

    # Validate that highest pair passes WCAG contrast ratio
    if max_contrast < WCAG_THRESHOLD:        
        if color_one.luminance > color_two.luminance:
            bright = [color_one, color_two]
        else:
            bright = [color_two, color_one]
        
        # Adjust luminance and saturation until meets WCAG_THRESHOLD

        while contrast.rgb(color_one.rgb, color_two.rgb) < WCAG_THRESHOLD:
            if bright[0].luminance < .95:
                bright[0].luminance += .0025
            if bright[1].luminance > .05:
                bright[1].luminance -= .0025
            if bright[0].luminance >= .95 and bright[1].luminance <= .05:
                if bright[0].saturation < .99:
                    bright[0].saturation += .01
                if bright[1].saturation > .02:
                    bright[1].saturation -= .0025
                if bright[0].saturation >= .99 and bright[1].saturation <= .02:
                    break
                
    # Collect colors not in highest contrast pair (foreground and background)
    secondary_colors = []
    for hexcode in color_list:
        if hexcode not in max_contrast_pair[1]:
            secondary_colors.append(hexcode)

    # Create 2 themes with foreground/background alternating values 
    style = "light"
    if color_one.luminance < .5:
        style = "dark"
    theme1 = {
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
        "background=" : color_one.hex_l,
        "foreground=" : color_two.hex_l,
        "tab=" : False,
        "style=" : style
    }

    if color_two.luminance < .5:
        style = "dark"
    theme2 = {
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
        "background=" : color_two.hex_l,
        "foreground=" : color_one.hex_l,
        "tab=" : False,
        "style=" : style
    }

    # Rank secondary colors on basis of contrast with bg color. Dict for each theme.
    contrast_with_bg = [
        {},
        {}
    ]
    for hexcode in secondary_colors:
        r = Color(hexcode)
        # Validate no rgb values over 1.0 
        r_adjusted = [1.0]*3
        for index, _ in enumerate(r.rgb):
            if _ < 1.0:
                r_adjusted[index] = _
        r_adjusted = tuple(r_adjusted)
        
        # keys are contrast value, values are hexcode
        rank = contrast.rgb(color_one.rgb, r_adjusted)
        contrast_with_bg[0][rank] = hexcode
        
        rank = contrast.rgb(color_two.rgb, r_adjusted)
        contrast_with_bg[1][rank] = hexcode

    # Fill in themes' colors in order of contrast with bg
    for contrast_lvl, color_num in zip(reversed(sorted(contrast_with_bg[0])), theme1.keys()):
        theme1[color_num] = contrast_with_bg[0][contrast_lvl]
    
    for contrast_lvl, color_num in zip(reversed(sorted(contrast_with_bg[1])), theme2.keys()):
        theme2[color_num] = contrast_with_bg[1][contrast_lvl]

    # Fill empty color slots by changing hue, saturation of highest contrast colors. Appraoch center
    # of list from both ends so highest contrast colors have priority for filling in empty slots.
        
    ret = [{},{}]

    for theme_index, theme in enumerate([theme1, theme2]):
        for index, (slot, hex) in enumerate(theme.items()):
            if not hex:
                filtered = []
                for code in theme.values():
                    if code:
                        if "#" in code:
                            filtered.append(code)
                filtered.reverse()
                filtered = filtered * 30
                syb = filtered[index]
                symmetric_sibling = Color(syb)
                #except:
                #   syb = theme1["foreground="]
                #  symmetric_sibling = Color(syb)
                upper_d = .98 - symmetric_sibling.saturation
                if upper_d > .01:
                    symmetric_sibling.saturation += random.uniform(.01, upper_d/4)

                upper_d = .98 - symmetric_sibling.luminance
                if upper_d > .01:
                    symmetric_sibling.luminance += random.uniform(.01, upper_d/2)
                ret[theme_index][slot] = symmetric_sibling.hex_l
            else:
                ret[theme_index][slot] = hex

    return ret