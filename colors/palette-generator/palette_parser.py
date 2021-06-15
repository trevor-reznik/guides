
import os
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


def main():
    random_name_index = 0
    html_files = locate_html()

    for html in html_files:
        raw = read_html(html)
        parsed_lines = parse_line_index(raw)
        hexcodes = parse_rgba(parsed_lines)

        for hex_list in hexcodes.values():
            themes = contrast_check(hex_list)
            themes[0]["full name"] = random_title(random_name_index).replace("/","").replace("=","").replace("\\","")
            random_name_index += 1
            themes[1]["full name"] = random_title(random_name_index).replace("/","").replace("=","").replace("\\","")
            random_name_index += 1
            make_theme_file(themes[0])
            make_theme_file(themes[1])

    move_files()


if __name__ == "__main__":
    main()