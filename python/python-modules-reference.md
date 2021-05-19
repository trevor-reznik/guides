<a name="table-of-contents"/>

# Python Modules Reference

- [**pip**](#pip)
- [**requests**](#requests)
- [**colorama**](#colorama)
- [**argparse**](#argparse)
- [**beautiful-soup**](#beautiful-soup)


----------------------------------------------------


<a name="pip"/>

### PIP
pip3 --version


<a name="requests"/>

### REQUESTS
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs.


<a name="colorama"/>

### COLORAMA
print in different colors


<a name="argparse"/>

### ARGPARSE


```python
def g_args():

    """""""""""""""
    |               # max space = 80, always one extra padding line, quotation quote # algorithm
    |                   
    |  add_argumnet()   
    |                   
    |
    |___________________________________________________________________________________________________ 
    |  [-]----------------------------------------------------------------------------------------------| 
    |  [1] name or flags :  Either a name or a list of option strings, e.g. foo or -f, --foo            |
    |  [+]______________________________________________________________________________________________| 
    |  [2] action        :  Basic type of action to be taken when this argument is encountered at       |
    |  [+]                  the command line                                                            |
    |  [+]______________________________________________________________________________________________| 
    |  [3] nargs         :  The number of command-line arguments that should be consumed                |
    |  [+]______________________________________________________________________________________________| 
    |  [4] const         :  A constant value required by some action and nargs selections               |
    |  [+]______________________________________________________________________________________________| 
    |  [5] default       :  The value produced if the argument is absent from the command line an       |
    |  [+]                  if it is absent from the namespace object                                   |
    |  [+]                  the argument is absentm the namespace object                                |
    |  [+]______________________________________________________________________________________________| 
    |  [6] type          :  The type to which the command-line argument should be converted             | 
    |  [+]______________________________________________________________________________________________| 
    |  [7] choices       :  A container of the allowable values for the argument                        |
    |  [+]______________________________________________________________________________________________| 
    |  [8] required      :  Whether or not the command-line option may be omitted (optionals only       |
    |  [+]______________________________________________________________________________________________| 
    |  [9] help          :  A brief description of what the argument does                               |
    |  [+]______________________________________________________________________________________________| 
    |  [a] metavar       :  A name for the argument in usage messages                                   |
    |  [+]______________________________________________________________________________________________| 
    |  [b] dest          :  The name of the attribute to be added to the object returned by parse_args()|
    |  [+]______________________________________________________________________________________________| 
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    parser = argparse.ArgumentParser(prog="juice")

    # Positional
    parser.add_argument("path", nargs="?")
    # Adjustments
    parser.add_argument("--downscale", "-d", nargs="?", const=1, type=int, default=0, metavar=("increment"))
    parser.add_argument("--title","-t", nargs="?", metavar=("title/header string"), default="none")
    # Output
    parser.add_argument("--rewrite","-r", action="store_true", default=False)
    parser.add_argument("--no-backup", action="store_true", default=False)
    parser.add_argument("--output", "-o", nargs="?", metavar=("path/name"), type=str, default="__FORMATTER-OUTPUT.txt", const="__FORMATTER-OUTPUT.txt")
    parser.add_argument("--open", nargs="?", type=str, choices=["gedit","vim", "nano", "office","cat", "notepad", "notepad++", "vscode", "sublime", "geany", "emacs", "docviewer", "browser", "pdf", "meld", "diff", "$filetype$"], metavar=("program|filetype"), default="gedit", const="gedit")
    # Figlet Choices
    parser.add_argument("-fonts","-f", nargs=4, default=["auto", "auto", "auto", "auto"], metavar=("[header]", "[section-titles]", "[special]", "[table-titles]"))
    parser.add_argument("--title-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    parser.add_argument("--section-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    parser.add_argument("--special-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    parser.add_argument("--table-title-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    # Additional Help Dialogs
    parser.add_argument("--show-fonts", action="store_true", default=False)

    return parser.parse_args()


# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


def main():
    options = vars(g_args())
```

<a name="beautiful-soup"/>

### BEAUTIFUL SOUP
Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
