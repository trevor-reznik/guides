"""
TODO:
    https://docs.gitlab.com/ee/user/markdown.html#gitlab-specific-references
"""

import sys
import os
NEWLINE = ["\n"]
LEADER = "  "


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
    # and add markdown="span" to the opening summary tag like this: <summary markdown="span">.

    # Remember to leave a blank line after the </summary> tag and before the </details> tag, as shown in the example:
    def __init__(self, input_file_name):
        pass

    def inline_diff(self):
        return """- {+ addition 1 +}
    - [+ addition 2 +]
    - {- deletion 3 -}
    - [- deletion 4 -]"""

    def task_list(self, ul):
        x = """- [x] Completed task
    - [ ] Incomplete task
    - [ ] Sub-task 1
    - [x] Sub-task 2
    - [ ] Sub-task 3

    1. [x] Completed task
    1. [ ] Incomplete task
    1. [ ] Sub-task 1
    1. [x] Sub-task 2"""


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


class Section:
    def __init__(self, first_line, all_lines, start_index):
        self.start_index = start_index
        self.all_lines = all_lines
        self.slice_title()
        self.parse_title()
        self.tier = first_line.count("#")

        self.url = self.encode_href(self.formatted_title)
        self.href_html = self.format_href(self.url)
        self.need_href = self.href_already_exists()

    def slice_title(self):
        i = self.start_index
        while not self.all_lines[i].startswith("#") and i < 3:
            i += 1
        while self.all_lines[i] and self.all_lines[i] != "\n":
            i += 1
        self.title = "".join(self.all_lines[:i]).replace("#", "").strip().strip("\n").strip()
        self.content = self.all_lines[i:]

    def parse_title(self):
        strip_chars = ["\n", " "]
        self.formatted_title = (self.title).replace("#", "")
        for char in strip_chars:
            self.formatted_title = self.formatted_title.strip(char)

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

    def href_already_exists(self):
        index = self.start_index
        while index > 0:
            curr_line = self.all_lines[index - 1]
            if (
                len(curr_line.strip("\n")) > 2
                and "-------" not in curr_line
            ):
                return (
                    True if "<a name=" in curr_line
                    else False
                )
            index -= 1
        return False


class SubDocument:
    def __init__(self, lines):
        self.title = lines[0]
        self.reference = self.title.strip(" ").split(" ")[1].replace("\n", "")
        self.lines = lines[1:]
        self.toc_head = [
            f'<a name="table-of-contents-{self.reference}"/>',
            "\n"
        ]

        self.footer_title = "###### Footnotes"
        self.to_top_link = (
            "\n\n-----------------------------\n\n"
            + "<div align=\"center\" style=\"font-size:"
            + " 11px; margin: 0; opacity:.6\"><a href=\""
            + f"#table-of-contents-{self.reference}"
            + "\">Top (目次)</a></div>\n "
        )
        self.to_absolute_top_link = (
            "\n\n-----------------------------\n\n"
            + "<div align=\"center\" style=\"font-size:"
            + " 11px; margin: 0; opacity:.6\"><a href=\""
            + "#table-of-contents"
            + "\">Very Top (目次)</a></div>\n\n\n"
        )

        self.sections = []
        self.toc = []
        self.footnotes = []

        self.parse_sections()
        self.create_toc()

    def join_footer(self):
        if len(self.footnotes) > 0:
            return (
                [self.footer_title]
                + NEWLINE
                + self.footnotes
                + NEWLINE
            )
        return []

    def get_output(self):
        out = (
            [self.title]
            + NEWLINE
            + self.toc_head
            + NEWLINE
            + self.toc
            + NEWLINE
            + self.content
            + NEWLINE
            + self.join_footer()
            + NEWLINE
            + [self.to_absolute_top_link]
        )
        # if len(self.content) > 150:
        #      out = [self.to_top_link]
        return out

    def footnote(self, text, index):
        start = f"{text} [^{index}]"
        end = f"[^footnote-{index}]"
        self.footnotes.append(end + "\n")
        return start

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

    def create_toc(self):
        if not self.sections:
            return []

        ticker = RelativeTicker(self.sections[0].tier)
        for section in self.sections:
            self.toc.append(
                f"{self.tabs(ticker.rel_tier)}- "
                + f"[{self.toc_decoration(section.title, ticker)}]"
                + f"(#{section.url})\n"
            )

    def parse_sections(self):
        self.content = []
        inline_code = False
        for index, line in enumerate(self.lines):
            if line.startswith("```"):
                inline_code = not inline_code
            if line.startswith("#") and not inline_code:
                if index > 150:
                    self.content.append(self.to_top_link)
                section = Section(line, self.lines, index)
                if section.need_href:
                    self.content.append(section.href_html)
                self.sections.append(section)

            self.content.append(line)


class CollapsibleSection:
    def __init__(self, first_line, all_lines, first_line_index):
        self.first_line = first_line
        self.tier = first_line.count("#")
        self.title = first_line.replace("\n", "").replace("#", "").strip()
        self.all_lines = all_lines
        self.start_index = first_line_index
        self.summary_open = [
            "\n",
            "\n<details>\n",
            '   <summary><b> ',
            self.first_line.replace("#", "").strip(),
            " </b></summary>"
        ]
        self.summary_close = [
            "\n\n",
            "\n</details>\n",
        ]

        self.url = self.encode_href(self.title)
        
        # Init.
        self.parse_content()

    def get_output(self):
        return (
            NEWLINE
            + self.summary_open
            + NEWLINE
            + NEWLINE
            + self.content
            + NEWLINE
            + self.summary_close
            + NEWLINE
        )

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

    def parse_content(self):
        self.end_index = self.start_index + 1
        top_section_id = "#" * self.tier

        while (
            self.end_index < len(self.all_lines)
            and top_section_id not in self.all_lines[self.end_index] 
        ):
            self.end_index += 1
        subdoc = SubDocument(self.all_lines[self.start_index : self.end_index])
        self.content = subdoc.get_output()


class MDDocument:
    def __init__(self, file_name, options={}):
        self.config = {
            "backup_loc": "here",
            "original work": True,
            "backup": True
        }
        self.config.update(options)
        self.file = file_name

        self.lines = self.no_whitespace(
            open(self.file, "r")
            .readlines()
        )
        if self.config["backup"]:
            self.backup()

        self.toc_head = [
            '<a name="table-of-contents"/>\n',
            "\n",
            "###### Table of Contents\n"
            "\n"
        ]

        self.config_tag = '{::options parse_block_html="true" /}\n'

        self.footer_decoration = ""
        if self.config["original work"]:
            self.footer_decoration += (
                '<div align="center" style="text-align: '
                + 'center; font-family: monospace; allign: center">\n'
                + 'Made with <g-emoji class="g-emoji" alias="heart" '
                + 'fallback-src="'
                + 'https://github.githubassets.com/images/icons/emoji/unicode/2764.png">'
                + '\n   <img class="emoji" alt="heart" height="20" width="20" src="'
                + 'https://github.githubassets.com/images/icons/emoji/unicode/2764.png">'
                + '</g-emoji>\n <a href="https://www.bymyself.life">bymyself</a>'
                + '</div>\n\n<div align="center" style="font-size: 11px; margin: 0; '
                + 'opacity:.6"> <a href="#table-of-contents">Top (目次)</a>\n</div>'
            )
        else:
            self.footer_decoration += (
                "\n\n\n-----------------------------\n\n"
                + "<div align=\"center\" style=\"font-size:"
                + " 11px; margin: 0; opacity:.6\"><a href=\""
                + "#table-of-contents\">Top (目次)</a></div>\n "
            )

        self.output = []
        self.sections = []
        self.title = ""
        self.toc = []

        # "+++" if toml, ";;;" if json, "---php" if php.
        self.front_matter_delim = "---"
        self.front_matter = [
            self.front_matter_delim,
            f"title: {self.title}",
            f"permalink: ",
            f"published: ",
            f"category: ",
            f"tags: ",
            f"file: {file_name}",
            f"language: ",
            self.front_matter_delim
        ]

        self.slice_title()
        self.parse_sections()
        self.create_toc()

    def no_whitespace(self, lines):
        ret = []
        for line in lines:
            ret.append(line.strip(" "))
        return ret

    def overwrite(self):
        final = (
            [self.config_tag]
            + self.title
            + NEWLINE
            + self.toc_head
            + NEWLINE
            + self.toc
            + NEWLINE
            + self.output
            + NEWLINE
            + [self.footer_decoration]
            + NEWLINE
            + NEWLINE
        )
        test = open(self.file, "w")
        for line in final:
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

    def create_toc(self):
        ticker = RelativeTicker(self.sections[0].tier)
        for section in self.sections:
            self.toc.append(
                f"{self.tabs(ticker.rel_tier)}- "
                + f"[{self.toc_decoration(section.title, ticker)}]"
                + f"(#{section.url})\n"
            )

    def backup(self):
        parts = self.file.split("/")
        backup_file = os.path.join(
            *(parts[:-1] + ["BACKUP-" + os.path.basename(self.file)])
        )
        backup_file = open(backup_file, "w")
        for line in self.lines:
            backup_file.write(line)
        backup_file.close()

    def parse_sections(self):
        inline_code = False
        index = 0
        bound = len(self.lines)
        while index < bound:
            line = self.lines[index]

            if line.startswith("```"):
                inline_code = not inline_code

            if line.startswith("#") and not inline_code:
                section = CollapsibleSection(line, self.lines, index)
                self.output += section.get_output()
                
                self.sections.append(
                    section
                )
                index = section.end_index

            else:
                index += 1
                self.output.append(line)

    def slice_title(self):
        i = 0
        while not self.lines[i].startswith("#"):
            i += 1
        while self.lines[i] and self.lines[i] != "\n":
            i += 1
        self.title, self.content = self.lines[:i], self.lines[i:]
        self.title.append("\n")


def main():
    file_name = sys.argv[1]
    formatted = MDDocument(file_name)
    formatted.overwrite()


if __name__ == "__main__":
    main()
