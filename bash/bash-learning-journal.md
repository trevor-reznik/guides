# Learning Journals

<a name="table-of-contents"/>

##### Table of Contents
- [Bash](#bash)


<a name="bash"/>

### *Bash*


###### [9/12/2020] Figuring out how to copy wget's man-pages directly to my notes without Google - only manuals at hand

```bash
man -k copy
# found tool: cp

info cp

info wget --where                          # show location of man page for wget
# found location: /usr/share/info/wget.info.gz

man -k zip                                 # looking for function to cat a gz file
man -k zip | grep print
man -k zip | grep page
info | grep zip                            # try by looking for zip-related tools
# found tool: zmore

zmore ../../usr/share/info/wget.info.gz    # more'ing the man page to check if correct
# realization: zmore will not be good for piping output, need cat not more

man -k gzip                                # searching for a cat function for gzipped files
# found tool: zcat

zcat ../../usr/share/info/wget.info.gz     # testing by zcat'ing the man gz file
# success

zcat ../../usr/share/info/wget.info.gz > temp.txt; xdg-open temp.txt
# explanation: cat gz, redirect stdout to a temporary text file, open the text file

# want to find how to redirect to clipboard to be able to use while making guides/notes

man -k clipboard
# found tool: xclipboard

man xclipboard
info xclipboard
# failure: it is a program with a GUI

info xclipboard | grep SEE ALSO -A 3       # the manual mentions similar programs, get the names
# similar programs: X(7), xcutsel(1), xterm(1), 

man xcutsel
# failure: doesn't work (why??)

apt-cache search clipboard                              # search for external apps
apt-cahce search clipboard | grep GTK --exclude=xfce    # exlude xfce apps because on Ubuntu
# found external app: clipboard-cli

info npm                                   # using NPM to install
npm --help
sudo npm install -g clipboard-cli
cd; nano .bashrc -> alias cb=clipboard     # set an alias

# FINAL
zcat ../../usr/share/info/wget.info.gz | cp

# generalized command
zcat $MANUAL_PATH | clipboard-cli
```


# FUTURE RESEARCH

https://github.com/awesome-lists/awesome-bash
https://www.quora.com/What-is-the-most-useful-bash-script-that-you-have-ever-written
https://opensource.com/article/20/1/bash-scripts-aliases
https://linuxhint.com/30_bash_script_examples/
https://ostechnix.com/collection-useful-bash-scripts-heavy-commandline-users/
https://dev.to/aviaryan/some-helpful-bash-scripts-i-use-daily-40bd
https://www.8base.com/blog/the-simplest-productivity-hack-using-a-bash-script



