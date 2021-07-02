

import sys


def generate(lines):
    section_tiers = {}
    section_hyperlinks = {}

    ret_lines = []
    inline_code = False
    for index, line in enumerate(lines):

        if line.strip().startswith("```"):
            inline_code = not inline_code

        if line.strip().startswith("#") and not inline_code:
            title = line.strip("\n").strip().replace("#", "").strip()
            tier = line.count("#")
            section_tiers[title] = tier

            url = title.replace(" ", "-").lower().replace("\"", "").replace(
                "\'", "").replace("`", "").replace("\\", "").replace("/", "")
            section_hyperlinks[title] = url

            hyperlink = f'<a name="{url}"/>'

            try:
                previous_lines = [
                    lines[index-1],
                    lines[index-2],
                    lines[index-3],
                ]
            except IndexError:
                try:
                    previous_lines = [
                        lines[index-1],
                    ]
                except IndexError:
                    pass

            hyper_exists = False
            for prev in previous_lines:
                if "<a name=" in prev:
                    hyper_exists = True

            if not hyper_exists:
                ret_lines.append(hyperlink)
                ret_lines.append("\n")
                ret_lines.append("\n")
        ret_lines.append(line)

    return ret_lines, section_tiers, section_hyperlinks


def formatted_header():
    return [
        '<a name="table-of-contents"/>\n',
        "\n",
        "##### Table of Contents\n"
        "\n",
    ]


def formatted_footer(original_work):
    return """\n\n\n-----------------------------\n\n<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div>\n""" if not original_work else """---

#### Footnotes

[A-Z Index of Commands](https://ss64.com/bash/)

  <div align="center" style="text-align: center; font-family: monospace; allign: center">
    Made with <g-emoji class="g-emoji" alias="heart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png">
  <img class="emoji" alt="heart" height="20" width="20" src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png"></g-emoji> <a href="https://www.bymyself.life">bymyself</a>
  </div>
  
<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div> """


def write_new(lines, file_name):
    test = open(file_name, "w")
    for line in lines:
        test.write(line)

    test.close()


def slice_title(lines):
    i = 0
    while not lines[i].strip().startswith("#"):
        i += 1
    while lines[i] != "\n":
        i += 1
    title, content = lines[:i], lines[i:]
    title.append("\n")
    return title, content


def create_table_contents(tiers, urls):
    ret = formatted_header()

    LEADER = "  "
    cur_leader = ""
    cur_tier = 1
    relative_tier = 1

    for index, (section, tier) in enumerate(tiers.items()):
        if tier > cur_tier:
            cur_leader += LEADER
            relative_tier += 1
            cur_tier = tier
        elif tier < cur_tier:
            cur_leader = cur_leader[:-2]
            relative_tier -= 1
            cur_tier = tier

        decoration = {
            1: f"**{section.upper()}**",
            2: f"***{section.capitalize()}***",
            3: f"{section.capitalize()}",
            4: f"*{section.capitalize()}*",
            5: f"{section.lower()}",
            6: f"*{section.lower()}*",
            7: f"{section.lower().replace(' ', '-')}"
        }
        line = f"{cur_leader}- [{decoration[relative_tier]}](#{urls[section]})\n"
        ret.append(line)

    return ret


def backup(file_name):
    # create backup
    import os
    parts = file_name.split("/")
    backup_file = os.path.join(
        *(parts[:-1] + ["BACKUP-" + os.path.basename(file_name)])
    )
    write_new(
        open(file_name, "r").readlines(),
        backup_file
    )


def main(file_name=False, original_work=False, create_backup=False):
    if not file_name:
        file_name = sys.argv[1]
    if create_backup:
        backup(file_name)
    lines = open(file_name, "r").readlines()
    title, content = slice_title(lines)
    content, tiers, urls = generate(content)
    NEWLINE = ["\n"]
    joined = (
        NEWLINE
        + NEWLINE
        + title
        + create_table_contents(tiers, urls)
        + NEWLINE
        + content
        + NEWLINE
        + [formatted_footer(original_work)]
    )
    write_new(
        joined,
        file_name
    )


if __name__ == "__main__":
    main(create_backup=True)
