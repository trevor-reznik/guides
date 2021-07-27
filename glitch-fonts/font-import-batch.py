

import os


files = os.listdir()

print(files)



for font in files:
    fontName = font.strip().replace("font-", "").replace("font", "").replace(".ttf", "").replace(".otf", "")
    formatted = "@font-face {\n" + f"font-family: {fontName};\n" + \
        f"src: url('{font}') format('truetype');\n" + "}"

    print(formatted)
    print()

