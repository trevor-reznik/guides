


import os


def format_fonts():
    files = os.listdir("fonts/stylized/")

    for font in files:
        name = os.path.basename(font).split(".")[0].replace(" ", "-")
        a = '@font-face {\n' + 'font-family: ' + name + ';\nsrc: url(\"fonts/stylized/' + font + '\") format(\'truetype\');\n}'
        print(a)


one = """.close {
  background-image: url("close_focused_normal.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-color: transparent;
  background-position: center;
  margin: 0;
  padding: 0;
  aspect-ratio: 1 / 1;
}"""

def format_icons():
    files = os.listdir("icons/")

    for icon in files:
        name = os.path.basename(icon).split(".")[0].replace(" ", "-")

        a = f".{name}"
        a += " {\n  background-image: url('"
        a += f"icons/{icon}');"
        a += "\n"
        a += """  background-size: contain;
  background-repeat: no-repeat;
  background-color: transparent;
  background-position: center;
  margin: 0;
  padding: 0;
  aspect-ratio: 1 / 1;
}"""
        print(a)
        print()
         
        
format_icons()