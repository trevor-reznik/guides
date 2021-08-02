import sys
import os
NEWLINE = ["\n"]
LEADER = "  "

# https://docs.gitlab.com/ee/user/markdown.html#gitlab-specific-references


class Section:
    def __init__(self, first_line, all_lines, first_line_index):
        self.title = self.parse_title(first_line)
        self.tier = first_line.count("#")
        self.url = self.encode_href(self.title)
        self.href_html = self.format_href(self.url)
        self.need_href = self.href_already_exists(
            all_lines,
            first_line_index
        )

    def parse_title(self, line):
        title = line[:]
        exclude = ["#"]
        strip_chars = ["\n", " "]
        for char in exclude:
            title = title.replace(char, "")
        for char in strip_chars:
            title = title.strip(char)

        return title  # uneccessary

    def encode_href(self, text, extra=[], replace_options={}):
        exclude_list = ["\"", "\'", "`", "\\", "/"]
        replace_map = {
            " ": "-"
        }
        for char in exclude_list + extra:
            text = text.replace(char, "")

        replace_map.update(replace_options)
        for char, after in replace_map.items():
            text = text.replace(char, after)
        return text

    def format_href(self, url):
        hyperlink = f'<a name="{url}"/>'
        return "\n\n" + hyperlink + "\n\n"

    def href_already_exists(self, lines, start_index):
        index = start_index
        while index > 0:
            curr_line = lines[index - 1]
            if (
                len(curr_line.strip("\n")) > 2
                and "-------" not in curr_line
            ):
                return (
                    True if "<a name=" in curr_line
                    else False
                )
            index -= 1


class RelativeTicker:
    def __init__(self, first_tier_n):
        self.rel_tier = 1
        self.recent = first_tier_n

    def increment(self, next_tier):
        if next_tier > self.recent:
            self.rel_tier += 1
            self.recent = next_tier
        elif next_tier < self.recent:
            self.rel_tier -= 1
            self.recent = next_tier


def formatted_footer(original_work):
    return """\n\n\n-----------------------------\n\n<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div>\n""" if not original_work else """---

#### Footnotes

[A-Z Index of Commands](https://ss64.com/bash/)

  <div align="center" style="text-align: center; font-family: monospace; allign: center">
    Made with <g-emoji class="g-emoji" alias="heart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png">
  <img class="emoji" alt="heart" height="20" width="20" src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png"></g-emoji> <a href="https://www.bymyself.life">bymyself</a>
  </div>
  
<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div> """


class MDDocument:
    def __init__(self, file_name, options):
        self.config = {
            "backup_loc": "here"
        }
        self.config.update(options)

        self.lines = self.no_whitespace(
            open(file_name, "r")
            .readlines()
        )

        title, content = slice_title(lines)
        sections, content = parse_sections(content)

        # "+++" if toml, ";;;" if json, "---php" if php.
        self.front_matter_delim = "---"
        self.front_matter = [
            self.front_matter_delim,
            f"title: About Front Matter",
            f"permalink: ",
            f"published: ",
            f"category: ",
            f"tags: ",
            f"file: {file_name}",
            f"language: ",
            self.front_matter_delim
        ]

        joined = (
            NEWLINE
            + title
            + NEWLINE
            + create_toc(sections)
            + NEWLINE
            + content
            + NEWLINE
            + [formatted_footer(original_work)]
            + NEWLINE
        )
        write(
            joined,
            file_name
        )

    def formatted_header():
        return [
            '<a name="table-of-contents"/>\n',
            "\n",
            "###### Table of Contents\n"
            "\n",
        ]

    def no_whitespace(self, lines):
        ret = []
        for line in lines:
            ret.append(line.strip(" "))
        return ret

    def write(self, lines, file_name):
        test = open(file_name, "w")
        for line in lines:
            test.write(line)
        test.close()

    def toc_decoration(self, section, ticker):
        decoration = {
            0: f"**__{section.upper()}__**",
            1: f"**{section.upper()}**",
            2: f"***{section.capitalize()}***",
            3: f"{section.capitalize()}",
            4: f"*{section.capitalize()}*",
            5: f"{section.lower()}",
            6: f"*{section.lower()}*",
            7: f"{section.lower().replace(' ', '-')}"
        }
        return decoration[ticker.rel_tier]

    def tabs(self, count):
        return (count - 1) * LEADER

    def create_toc(self, sections):
        ticker = RelativeTicker(sections[0].tier)
        for section in sections:
            ret.append(
                f"{tabs(ticker.rel_tier)}- "
                + f"[{toc_decoration(section.title, ticker)}]"
                + f"(#{section.url})\n"
            )

        return ret

    def backup(self, file_name):
        parts = file_name.split("/")
        backup_file = os.path.join(
            *(parts[:-1] + ["BACKUP-" + os.path.basename(file_name)])
        )
        self.write(
            open(file_name, "r").readlines(),
            backup_file
        )

    def parse_sections(self, lines):
        sections = []
        ret_lines = []
        inline_code = False
        for index, line in enumerate(lines):
            if line.startswith("```"):
                inline_code = not inline_code
            if line.startswith("#") and not inline_code:
                section = Section(line, lines, index)
                if section.need_href:
                    ret_lines.append(section.href_html)
                    sections.append(section)
            ret_lines.append(line)
        return sections, ret_lines

    def slice_title(self, lines):
        i = 0
        while not lines[i].startswith("#"):
            i += 1
        while lines[i] and lines[i] != "\n":
            i += 1
        title, content = lines[:i], lines[i:]
        title.append("\n")
        return title, content


class HTMLMarkup:
    def __init__(self):
        pass

    def bolden(self, text):
        return f"<strong>{text}</strong>"

    def italicize(self, text):
        return f"<em>{text}</em>"

    def wrap_code(self, text):
        return f"<pre><code>{text}</code></pre>"


class Formatter:
    # If your Markdown isn’t rendering correctly, try adding {::options parse_block_html="true" /} to the top of the page,
    # and add markdown="span" to the opening summary tag like this: <summary markdown="span">.

    # Remember to leave a blank line after the </summary> tag and before the </details> tag, as shown in the example:
    def __init__(self, input_file_name):
        self.footnotes = []

    def footnote(self, text, index):
        start = f"{text} [^{index}]"
        end = f"[^footnote-{index}]"
        return start, end


def inline_diff():
    return """- {+ addition 1 +}
- [+ addition 2 +]
- {- deletion 3 -}
- [- deletion 4 -]"""


def auto_toc():
    return "[[_TOC_]]"


def task_list(ul):
    x = """- [x] Completed task
- [ ] Incomplete task
  - [ ] Sub-task 1
  - [x] Sub-task 2
  - [ ] Sub-task 3

1. [x] Completed task
1. [ ] Incomplete task
   1. [ ] Sub-task 1
   1. [x] Sub-task 2"""
    pass


def main(file_name=False, original_work=False, create_backup=False):
    if not file_name:
        file_name = sys.argv[1]


if __name__ == "__main__":
    main(create_backup=True)
