

import sys

def generate(file_name=False):
    if not file_name:
        file_name = sys.argv[1]
    md = open(file_name, "r").readlines()
    section_names = []
    for line in md:
        if "<a name=" in line:
            parsed = line.split('<a name="')[1]
            section_names.append(
                parsed.split('"')[0]
            )
    print(
        '<a name="table-of-contents"/>',
        "",
        "",
        "##### Table of Contents"
        "",
        sep="\n"
    )
    for name in section_names:
        capitalized = " ".join(
            [word[0].upper() + word[1:] for word in name.replace("\n","").replace("-", " ").split()]
        )
        print(
            f"- [**{capitalized}**](#{name})"
        )
    

if __name__ == "__main__":
    generate()