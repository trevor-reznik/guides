import os
themes = os.listdir("/home/bymyself/p/g/colors/palette-generator/themes/")


def roll_random_theme():
    import random
    r_index = random.randint(0, len(themes))
    theme = themes[r_index]
    return theme


def new_term_w_random():
    random_theme = roll_random_theme() 
    print(f"Loaded random theme called: {random_theme}")
    os.system(
        f"nohup >/dev/null deepin-terminal -l '{random_theme}' & disown \n"
    )

 
def switch_theme():
    config_file = open("~/.config/deepin/deepin-terminal/config.conf", "r")
    lines = config_file.readlines()
    config_file.close()
    new_config = open("~/.config/deepin/deepin-terminal/config.conf", "w")


if __name__ == "__main__":
    new_term_w_random()