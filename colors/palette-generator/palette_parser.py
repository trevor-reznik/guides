
import os, contrast_sorter
from random_words import random_title
from contrast_sorter import contrast_check


def wget_pages():
    os.system(
        "wget https://coolors.co/palettes/trending",
        "wget https://coolors.co/palettes/popular"
    )


def locate_html(base_path="./crawl_files/"):
    ret = []
    cd = os.listdir(base_path)
    for file in cd:
        if ".html" in file:
            print(f"[+] Located HTML file: {file}\n")
            ret.append(base_path + file)
    return ret


def read_html(file_name):
    file = open(file_name, "r")
    ret = file.readlines()
    file.close()
    print(f"[+] Read HTML file: {file_name}\n")

    return ret


def parse_line_index(html):
    ret = {}
    print("[~] Attempting to Parse file . . .\n")
    
    for index, line in enumerate(html):
        if "explore-palette_colors" in line:
            bgs_index = index
            try:
                while "background:" in html[bgs_index]:
                    bgs_index +=1
            except: pass

            ret[str(index)] = []
            for color_index in range(index, bgs_index):
                ret[str(index)].append(
                    html[color_index]
                )
    if ret:
        print("[+] Successfully Parsed Lines\n")

    return ret


def parse_rgba(html):
    
    print("[+] Parsing Color Codes from Lines\n")
    ret = {}

    for key, html_line in html.items():
        joined = " ".join(html_line)
        brk = joined.split("span")
        ret[key] = []

        for _ in brk:
            if len(_) == 9:
                hex = "#" + _.replace("<","").replace(">","").replace("/","")
                ret[key].append(hex)
    
    return ret


def make_theme_file(theme):
    name = theme["full name"]
    log = open("themes/" + name, "w")
    log.write("[theme]\n")

    for key, value in theme.items():
        if key != "full name":
            log.write(key + value.lower())
            log.write("\n")
    log.close()


def move_files():
    files = os.listdir("themes/")

    for _ in files:
        os.system(
            "sudo cp " + "themes/'" + _ + "' ~/../../usr/share/deepin-terminal/theme/"
        )


def main(shuffle_duplicates=True):
    random_name_index = 0
    html_files = locate_html()

    current_pairs = {}

    for html in html_files:

        print("[+] Creating Theme Files . . . \n\n\n")
        raw = read_html(html)
        parsed_lines = parse_line_index(raw)
        hexcodes = parse_rgba(parsed_lines)

        for hex_list in hexcodes.values():
            themes = contrast_check(hex_list)
            themes[0]["full name"] = random_title(random_name_index).replace("/","").replace("=","").replace("\\","")
            random_name_index += 1
            themes[1]["full name"] = random_title(random_name_index).replace("/","").replace("=","").replace("\\","")
            random_name_index += 1

            for theme in themes:
                bg, fg = theme["background="], theme["foreground="]

                new_color = True
                if bg in list(current_pairs.keys()):
                    if fg == current_pairs[bg]:
                        
                        if not shuffle_duplicates:
                            continue

                        new_color = False
                        duplicate_count = 0
                        for accent_tier in theme.values():
                            duplicate_count += 1
                            if accent_tier not in list(current_pairs.keys()):
                                new_color = accent_tier
                                print(f"\n[-] Theme Duplicated {duplicate_count} Times in List. Colors Swapped\n")
                                break
                        if new_color:
                            theme["background="] = new_color 
                
                if new_color:
                    make_theme_file(theme)
                    current_pairs[theme["background="]] = fg
                if not new_color:
                    print("\n\n\n\n[-] Duplicate Unresolved - Scheme Occurs over 16 Times in Passed List\n\n\n\n")


if __name__ == "__main__":
    #main(shuffle_duplicates=False)
    move_files()