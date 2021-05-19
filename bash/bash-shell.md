
<a name="table-of-contents"/>

![Pictures](bash-shell-usage.png)


---




## [Very Useful](#Highly) 

- [**History Expansion**](#history)
- [**Manuals / Info**](#manuals)
- [**Globbing / Searching**](#globbing)
- [**Hotkeys**](#navigation)
- [**Finding Tools**](#findtools)
- [**File Transfer**](#transfer)
- [**Redirecting & Piping**](#redirect)


## [Moderately Useful](#Moderately)

- [**Scraping Data**](#scraping)
  - [wget](#wget)
- [**Parsing Data**](#parsing)
  - [lynx](#lynx)
  - [awk](#awk)
  - [grep](#grep)
- [**Opening / Starting Files**](#opening/starting)
  - [finding things](#finding_things)
  - [opening things](#open)
    - [nano cheatsheet](#nanocheatsheet)
    - [vim cheatsheet](#vimcheatsheet)


## [Sometimes Very Useful](#SometimesVery)


- [**System Stats**](#system_stat)
  - [internal](#internal_stats)
  - [network](#network_stats)
  - [killing processes](#killing)


## [Sometimes Useful](#Sometimes)

- [**Compression**](#Compression)
  - [extracting](#extracting)
  - [compressing](#compressing)


## [Kind of Useful](#kindof)

- [**Shell Prompts**](#shell_prompts)




---

![Pictures](bash-shell-usage.png)




# Recent


###### Save password as environment variables

```bash
vim .bashrc
export PROGRAM_SECRET=$SECRET
:wq

echo $PROGRAM_SECRET | clipboard
```

###### Looking for file with keywords

```bash
cd; ls -R | grep $KEYWORD -B 30
```

```bash
grep --exclude=GLOB
```


```bash
Ctrl+R Keyword Search History
```


```bash
xdg-open $URL

xdg-open .
```


```bash
--prefix=sudo
```


```bash
tail
```


```bash
setvtrgb 
```

![List of Bash Commands](../info-pics/linux_commands.jpg)



<a name="Highly"/>


![Pictures](bash-shell-usage.png)


# HIGHLY USEFUL


<div align="right" position="absolute" font-size=12 margin=0 opacity= .6 margin-right=0 margin-left=75%><a href="#table-of-contents">Very Top (目次)</a></div> 


<a name="1-contents"/>


<div font-size=11 font-family=monospace>


- [History Expansion](#history)
- [Manuals / Info](#manuals)
- [Globbing / Searching](#globbing)
  - [match](#matching)
  - [exclude](#exclude)
- [Hotkeys](#navigation)
  - [navigation commands](#navigation_commands)
  - [editing commands](#editing_commands)
  - [processes commands](#processes_commands)
  - [history commands](#historycommands)
- [Finding Tools](#findtools)
- [File Transfer](#transfer)
- [Redirecting](#redirect)

<a name="history"/>


### History Expansion 


###### Execute most-recent command containing a `$KEYWORD` or a `$PREFIX`


```bash
!?$KEYWORD?

!$PREFIX 
```


###### Prefix/Shift `$KEYWORD` to previous command then execute


```bash
$KEYWORD !!
```
```bash
sudo !!                             # repeat last cmd w/ sudo prefixed

cd $CORRECT_LOC; !!					# cd to correct location then repeat previous command
```


###### Replace `$WORD` with `$NEW_WORD` in previous command then execute


```bash
^$WORD^$NEW_WORD                    # most-recent command

!?$KEYWORD?:s/$WORD/$NEW_WORD/      # most-recent command containing $KEYWORD
```


###### Reference Previous Arg(s)


```bash
$NEW_CMD !$                     # reference last arg

$NEW_CMD !*                     # reference all args

$NEW_CMD !:$NUM                 # reference arg by number

$NEW_CMD !:$NUM-$NUM            # reference range of args
```


###### Reference Previous Commands by Number


```bash
!$NUM                               # stands for cmd #$NUM - e.g., !$1800 = command 1800

!-$NUM                              # stands for command that is $NUM of commands back from current
```


###### Search History for Previous Command or for Command Numbers


```bash
CTRL-R

history                             

export PS1="\!$ "                   # put cmd # in prompt so you don't need to Ctrl-R or use 'history'
```


-----


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>


<a name="manuals"/>

### Manuals / Help



###### Core Bash Docs


```bash
info coreutils
info bash
help help
```

###### Search for Manuals Related to `$KEYWORD`


```bash
man -k $KEYWORD|$FILE_EXT|$ETC              # also useful to find functions by keyword
```


###### See One-Line Manual/Summary of `$THING`


```bash
whatis $THING
```


###### See Usage and Options of `$THING`
 

```bash
$THING --help

    -d	output short description for each topic
    -m	display usage in pseudo-manpage format
    -s	output only a short usage synopsis for each topic matching
        PATTERN
```



###### View Annotated Options of `$THING`


```bash
man [OPTION...] $THING [PAGE]...
man man


	  -H, --html[=BROWSER]       use www-browser or BROWSER to display HTML output
	  -i, --ignore-case          look for pages case-insensitively (default)
		  --wildcard             show all pages matching wildcard
		  --names-only           make --regex and --wildcard match page names only,
		                         not descriptions
	  -K, --global-apropos       search for text in all pages
	  -w, --where, --path        print physical location of man page(s)
	  -S, -s, --sections=LIST    use colon separated section list
	  -a, --all                  find all matching manual pages
		  --no-subpages          dont try subpages, e.g. "man foo bar" => "man foo-bar"
```


###### Browse `$THING`'s Entire Manual by Section / Chapter
     

```bash
info [OPTION]... [MENU-ITEM...]

info $start_menu [relative-menu-items]


        --show-options
    -k, --apropos=STRING         look up STRING in all indices of all manuals
        --index-search=STRING    go to node pointed by index entry STRING
    -n, --node=NODENAME          specify nodes in first visited Info file
    -o, --output=FILE            output selected nodes to FILE
    -O, --show-options, --usage  go to command-line options node
    -w, --where, --location      print physical location of Info file
```

```bash
info coreutils | grep $KEYWORD$

info --subnodes -o out.txt emacs		# dump entire emacs manual to out.txt

info -f ./foo.info           			# show file ./foo.info, not searching dir
```




###### Search for Specific Option


```bash
$CMD --help | grep $KEYWORD

ls --help | grep recursive -A 2 -m 3
```





```bash
man -a intro                     		# Display, in succession, all of the available intro 
                                 		# manual pages contained within the manual
```

---

<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>


<a name="globbing"/>


### Globbing

<a name="match"/>

###### Match any Number of Characters (inc. zero)

```bash
* 

cp ~/project/static/*assets*/pic* .
```

###### Match any Single Character


```bash
?	

cp pic?.jpg
```


###### Match from List of Characters


```bash
fill[$CHARACTER,$CHARACTER,$CHARACTER]	# wildcard from list
ls [p,P]ictures
cd [config,.config,appconfig]

fill[$FROM_CHARACTER-$TO_CHARACTER]		# wildcard from range
cp pic[1-10].jpg .
ls [P-p]ictures

[$CHARACTER-!$EXCEPT]					# list with matches and exclusions
mv [!.,a-z]
cp pic[!1,!2,3,4].jpg

[$CHARACTER-!$EXCEPT]					# list with ranges of exclusions
rm pic[!1-10]							# delete all pics except 1 through 10

[:class:]                       		# by class using LC_TYPE POSIX standard variables
```

###### Extended Regular Expressions `extglob` *(often used in bash if statemetns with the `=~` operator)*


```bash
?($LIST)                        # 0-1 occurrence of list items

*($LIST)                        # 0-n occurrence of list items

+($LIST)                        # 1-n occurrence of list items

@($LIST)                        # 1 occurrence of list items

!($LIST)                        # anything but list items
```


###### Exclude

<a name="exclude"/>

```bash
$CMD $MATCH!($exclude)
echo rm foo.!(org)

[!a]                            # exclude a

[!a-d]                          # exclude from range a-d
```


----


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>


<a name="navigation"/>


### Hotkeys / Shortcuts


<a name="navigation_commands"/>

###### Navigation

| Command | Fuunction |
|:-------------:|:-------------|
Ctrl + A	        |Go to the beginning of the line.
Ctrl + E	        |Go to the end of the line.
Alt + F            |Move the cursor forward one word.
Alt + B	            |Move the cursor back one word.
Ctrl + F	        |Move the cursor forward one character.
Ctrl + B	        |Move the cursor back one character.
Ctrl + X, X	        |Toggle between the current cursor position and the beginning of the line.


<a name="editing_commands"/>

###### Editing	

| Command | Fuunction |
|:-------------:|:-------------|
Ctrl + _	        | Undo! (And, yes, that's an underscore, so you'll probably need to use Shift as well.)
Ctrl + X, Ctrl + E	| Edit the current command in your $EDITOR.
Alt + D             | Delete the word after the cursor.
Alt + Delete	    | Delete the word before the cursor.
Ctrl + D	        | Delete the character beneath the cursor.
Ctrl + H	        | Delete the character before the cursor (like backspace).
Ctrl + K	        | Cut the line after the cursor to the clipboard.
Ctrl + U	        | Cut the line before the cursor to the clipboard.
Ctrl + D	        | Cut the word after the cursor to the clipboard.
Ctrl + W	        | Cut the word before the cursor to the clipboard.
Ctrl + Y	        | Paste the last item to be cut.


<a name="processes_commands"/>

###### Processes	

| Command | Fuunction |
|:-------------:|:-------------|
Ctrl + L	        |Clear the entire screen (like the clear command).
Ctrl + Z	        |Place the currently running process into a suspended background process (and then use fg to restore it).
Ctrl + C	        |Kill the currently running process by sending the SIGINT signal.
Ctrl + D	        |Exit the current shell.
Enter, ~, .	        |Exit a stalled SSH session.


<a name="historycommands"/>


###### History	        


| Command | Fuunction |
|:-------------:|:-------------|
Ctrl + R	        |Bring up the history search.
Ctrl + G	        |Exit the history search.
Ctrl + P	        |See the previous command in the history.
Ctrl + N	        |See the next command in the history.


----

<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

<a name="findtools"/>


### Finding Tools to Solve Problems


###### Finding External Apps


```bash
apt-cache search $KEYWORD

apt-cache search $KEYWORD | grep $MORE_SPECIFIC_KEYWORD

info apt-cache
```
```bash
apt-cache search clipboard                          # find apps that provide clipboard-related tools

apt-cache search clipboard | grep xfce				# limit to xfce-specific clipboards/apps
```


###### Finding Built-in Functions Related to `$KEYWORD`


```bash
man -k $KEYWORD
man -k compress										# find built-in tools related to compression/extraction

info | grep $KEYWORD

info coreutils | grep $KEYWORD

help | grep $KEYWORD

# Display possible completions depending on the options.
compgen [-A action] [-W wordlist] [-F function] [-C command] [-P prefix] [-S suffix] [word]
```

----

<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>


<a name="transfer">

### File Transfer



###### Using SSH

```bash
scp $SOURCE $DESTINATION

scp [local_path] [remote_username@ip:/store_here]           # local -> remote
scp [remote_username@ip:/file] [local_path]                 # remote -> local

# cp B to A while logged into B
scp $PATH/$FILE $USERNAME@$IP:$PATH

# cp B to A while logged into A:
scp $USERNAME@$IP:$PATH/$FILE $PATH

      [-B bind_interface]
      [-b bind_address]	[-D [bind_address:]port] 
      [-J [user@]host[:port]] [-L address]
      [-o option] [-p port]
      [-R address] [-S ctl_path] [-W host:port]
      [-w local_tun[:remote_tun]] destination [command]

      [-c cipher_spec]  [-E log_file] 
      [-e escape_char] [-F configfile] [-I pkcs11]

      [-l login_name]  [-i identity_file] 
      [-m mac_spec] [-O ctl_cmd] [-Q query_option] 
```


```bash
# Troubleshoot
systemctl status ssh
ufw allow ssh
```

###### Using Secure SSH Transfer

```bash
pscp [options] source [source...] [user@]host:target    # local -> remote
pscp [options] [user@]host:source target                # remote -> local
```

###### Using rsync *(Local or Remote SSH/TCP)*


```bash
rsync <source_user>@<source_host>:<file> <destination_user>@<destination_host>:<file>

      --progress
      -r

# local to remote 
rsync file user@192.168.178.27:file

# remote host to local
rsync user@192.168.178.27:file file
```

###### Using FTP

```bash
ftp [-46pinegvd] [host [port]]

pftp [-46inegvd] [host [port]]
```

```bash
wget -r ftp://username:password@1.2.3.4/$dir$/*

wget -r ftp://1.2.3.4/dir/* --ftp-user=username --ftp-password=password  # shared servers
```

###### Using SFTP

```bash
sftp $USERNAME@$IP

      [-46aCfpqrv] [-B buffer_size] [-b batchfile] [-c cipher]
      [-D sftp_server_path] [-F ssh_config] [-i identity_file]
      [-J destination] [-l limit] [-o ssh_option] [-P port]
      [-R num_requests] [-S program] [-s subsystem | sftp_server]
      destination

# After Session is Established, in SFTP Nested Shell:
lcd $LOCAL_DIR
cd $REMOTE_DIR
lls                                         # view local dir
lpwd                                        # print local cd
lmkdir $DIR_NAME                            # make local dir

get $REMOTE_FILE							# get single file from remote's cd into local cd
put $LOCAL_FILE								# put single file from local cd into remote cd

mget *$MATCH                                # get all files from remote's cd using glob match
mget * -r $REMOTE_FILES                     # get all files and sub-dirs from remote's cd
mput * -r $LOCAL_FILES                      # put all local files and sub-dirs from lcd into remote's cd
```


----------

<div align="right" font-family="monospace">
    <b><a href="#cotents-1">↥ Back To Top</a></b>
</div>

<a name="replacing">

### Replacing

```bash
sed [OPTION]... {script-only-if-no-other-script} [input-file]...

# replaces “unix” with “linux” in the file
sed 's/unix/linux/' file.txt

  -i[SUFFIX], --in-place[=SUFFIX]
                 edit files in place (makes backup if SUFFIX supplied)
  -l N, --line-length=N
                 specify the desired line-wrap length for the l command
  -E, -r, --regexp-extended
                 use extended regular expressions in the script
                 (for portability use POSIX -E).
```


----------


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>


<a name="redirect">

### Redirecting and Piping


###### Redirecting or Piping Output


```bash
$CMD > $REDIRECT_DESTINATION
echo "hello" > file.txt
```

```bash
$CMD1  | $CMD2											# cmd1's output is used as cmd2's input
ls -l | sed -e "s/[aeio]/u/g"  
ls -l | grep "\.txt$"
```

```bash
cat file.txt | grep $KEYWORD > output.txt
```

###### Append Instead of Overwrite


```bash
$CMD >> $FILE
```


###### Redirect Input


```bash
$CMD < $ARG_FROM
cat < file.txt
```


###### Redirect as Arg *(redirect stdin to command as arg)*

 ```bash
xargs [OPTION]... COMMAND [INITIAL-ARGS]...

# Choose the insert location (even multiple times):
grep -r $KEYWORD | xargs -I '{}' cp '{}' ~/data/lidar/tmp-ajp2/

find /foo -maxdepth 1 -atime +366 -print0 | xargs -r0 sh -c 'mv "$@" /archive' move


  -i, --replace[=R]            replace R in INITIAL-ARGS with names read
                                 from standard input; if R is unspecified,
                                 assume {}
  -p, --interactive            prompt before running commands
```


###### Redirect to Clipboard *(clipboard-cli or xclip External Applications)*


```bash
$CMD $ARG|$FILE | [clipboard|xclip]                              
```


```bash
# get location of thing's man page | cat the .tz file | filter with grep | pipe to cliboard
info $THING --where | xargs zcat | grep $TOPIC --exclude=$X -A $# | clipboard

# lynx dump webpage | search for phrase | pipe to cliboard
lynx -dump -listonly $URL | grep -v $KEYWORD | clipboard

# wget wikipedia page to stdout | remove html <tags> with sed and regex | 
# grep first instance of $SECTION + 30 lines after | pipe to cliboard
wget -qO- https://en.wikipedia.org/wiki/Mercer_Island | \
  sed -e 's/<[^>]*>//g' | grep $SECTION -m 1 -A 30 | clipboard

# append to file 
info $APPLICATION --where | xargs zcat >> ~/guides/*topic*
```

```bash
# Redirecting to Clipboard On Windows Git Bash (built-in tool)
cat file > /dev/clipboard                           # copy
clip < $FILE                                        # copy
cat /dev/clipboard > file                           # paste
```


<a name="Moderately"/>


<div align="right" position="absolute" font-size=12 margin=0 opacity= .6 margin-right=0 margin-left=75%><a href="#table-of-contents">Very Top (目次)</a></div> 


![Pictures](bash-shell-usage.png)



# MODERATELY USEFUL


<a name="Moderately"/>

- [SCRAPING DATA](#scraping)
  - [wget](#wget)
- [PARSING DATA](#parsing)
  - [grep](#grep)
  - [lynx](#lynx)
  - [awk](#awk)
- [OPENING / STARTING FILES](#opening/starting)
  - [Finding Things](#finding_things)
  - [Opening Things](#open)
    - [reading from terminal](#readinginsideterminal)
    - [writing from terminal](#writinginsideterminal)
      - [nano](#nano)
      - [vim](#vim)
        - [cursor](#vimcursor)
        - [cut & paste](#vimcutpaste)
        - [insert](#viminsert)
        - [editing](#vimediting)
        - [visual](#vimvisual)
        - [replace](#vimreplace)
        - [indent](#vimindent)
        - [registers](#vimregisters)
        - [marks](#vimmarks)
        - [macros](#vimmacros)
        - [diff](#vimdiff)
        - [window](#vimwindow)
        - [tabs](#vimtabs)
        - [exiting](#vimexiting)

<a name="scraping"/>

### Scraping


<a name="wget"/>

###### Get from Web


```bash
youtube-dl $VID_URL											# just video(s) or audio
```

```bash
gallery-dl $PIC_URL											# just picture(s)
```

```bash
wget $URL                               # all data

# 45 tries , log file, run in background
wget -t 45 -o log http://fly.srk.fer.hr/jpg/flyweb.jpg &

# FTP
wget ftp://gnjilux.srk.fer.hr/welcome.msg

# list of links from batch file
wget -i $FILE

# list of links from stdin
wget -i - $LINKS

# Create a five levels deep mirror image of $SITE converting links
wget --convert-links  -r $SITE -o gnulog
```
  

----

<div align="right" font-family="monospace">
    <b><a href="#Moderately">↥ Back To Top</a></b>
</div>


<a name="parsing"/>

### Parsing

<a name="grep"/>

###### Filtering Data/Output 


```bash    
grep $KEYWORD$

    -m, --max-count=NUM       stop after NUM selected lines
    -n, --line-number         print line number with output lines
        --line-buffered       flush output on every line
    -H, --with-filename       print file name with output lines
    -h, --no-filename         suppress the file name prefix on output
    -o, --only-matching       show only nonempty parts of lines that match
    -d, --directories=ACTION  how to handle directories;
                            ACTION is 'read', 'recurse', or 'skip'
    -D, --devices=ACTION      how to handle devices, FIFOs and sockets;
                            ACTION is 'read' or 'skip'
    -r, --recursive           like --directories=recurse
    -R, --dereference-recursive  likewise, but follow all symlinks
        --include=GLOB        search only files that match GLOB (a file pattern)
        --exclude=GLOB        skip files that match GLOB
        --exclude-from=FILE   skip files that match any file pattern from FILE
        --exclude-dir=GLOB    skip directories that match GLOB
    -L, --files-without-match  print only names of FILEs with no selected lines
    -l, --files-with-matches  print only names of FILEs with selected lines
    -c, --count               print only a count of selected lines per FILE

    # Context Control
        --color[=WHEN]
    -B, --before-context=NUM  print NUM lines of leading context
    -A, --after-context=NUM   print NUM lines of trailing context
    -C, --context=NUM         print NUM lines of output context
    -NUM                      same as --context=NUM
        
```


<a name="lynx"/>

###### Web Search


Lynx  is  a  fully-featured  World  Wide  Web  (WWW)  client.  
It will display HTML documents containing  links to  files  residing  on  the  local or systems
running Gopher, HTTP, FTP, WAIS, and NNTP servers.


Lynx  can  be used to access information on the World Wide Web, or to build information
systems intended primarily for local access.  For example, Lynx has been used to  build
several Campus Wide Information Systems (CWIS).  In addition, Lynx can be used to build
systems isolated within a single LAN.


```bash
lynx [options] [file]


	  -auth=id:pw       authentication information for protected documents
	  -index=URL        set the default index file to URL
	  -traversal        traverse all http links derived from startfile
	  -crawl            with -traversal, output each page to a file
		                with -dump, format output as with -traversal, but to stdout
	  -realm            restricts access to URLs in the starting realm (off)
	  -buried_news      toggles scanning of news articles for buried references (on)
	  -newschunksize=NUMBER
		                number of articles in chunked news listings
	  -nobrowse         disable directory browsing

	  -image_links      toggles inclusion of links for all images (off)


	  -convert_to=FORMAT
	  -underline_links  
	  -prettysrc        do syntax highlighting and hyperlink handling in source view (off)
	  -width=NUMBER     screen width for formatting of dumps (default is 80)
	  -number_fields    force numbering of links as well as form input fields (off)
	  -number_links     force numbering of links (off)
	  

	  -cookie_file=FILENAME
		                specifies a file to use to read cookies
	  -cookie_save_file=FILENAME
		                specifies a file to use to store cookies
	  -cookies          toggles handling of Set-Cookie headers (on)
	  -forms_options    toggles forms-based vs old-style options menu (on)
	  

	  -session=FILENAME resumes from specified file on startup and
		                saves session to that file on exit
	  -sessionin=FILENAME
		                resumes session from specified file
	  -sessionout=FILENAME
		                saves session to specified file
	  -show_cfg         Show "LYNX.CFG" setting (off)
	  -verbose          toggles [LINK], [IMAGE] and [INLINE] comments
		                with filenames of these images (on)


	  -get_data         user data for get forms, read from stdin,
		                terminated by '---' on a line
	  -post_data        user data for post forms, read from stdin,
	  -head             send a HEAD request (off)
	  
	  
	  -cmd_script=FILENAME
		                read keystroke commands from the given file
		                (see -cmd_log)
	  -dump             dump the first file to stdout and exit
	  -exec             enable local program execution
	  -source           dump the source of the first file to stdout and exit
```


<a name="awk"/>


###### Pattern Scanning and Processing Language


```bash
awk -f program-file [ -- ] file ...


    -f progfile		--file=progfile
    -F fs			--field-separator=fs
    -v var=val		--assign=var=val
    -b			--characters-as-bytes
    -d[file]		--dump-variables[=file]
    -D[file]		--debug[=file]
    -e 'program-text'	--source='program-text'
    -i includefile		--include=includefile
    -l library		--load=library
    -N			--use-lc-numeric
    -n			--non-decimal-data
    -o[file]		--pretty-print[=file]
    -O			--optimize
    -p[file]		--profile[=file]
    -P			--posix
    -t			--lint-old
```


###### Diff

```bash
vim -d $FILE1 $FILE2
```

###### Batch .Ext Change

```bash
for f in *.md; do mv "$f" "${f%.md}"; done; for f in *; do mv "$f" "$f.md"; done
```

---


<div align="right" font-family="monospace">
    <b><a href="#Moderately">↥ Back To Top</a></b>
</div>


<a name="opening/starting"/>


### Opening / Starting


<a name="finding_things"/>


###### Finding Files / Apps


```bash
locate [option(s)] file_name(s)

ls | grep *$KEYWORD$* -m 1 | xargs find | grep $KEYWORD$ -m 1

find [-H] [-L] [-P] [-D DEBUGOPTIONS] [-OLEVEL] [FILE...] [KEYWORD]

find . -type f -path '*SCHEDULE*/*' -name '*.xls'

dpkg -l | grep $RELATED_KEYWORD                                               # find the name of a package
dpkg --list
```

###### Locate Binary, Source and Man files for `$CMD`


```bash
whereis $CMD
```

<a name="open"/>


###### Open File


```bash
xdg-open $FILE
```

###### Open URL


```bash
xdg-open $URL
```

###### Opening and Disowning


```bash
&   &&
&                                         # run previous in background and run next cmd immediately after

disown                                    # disown shells' processes                

nohup $CMD                                # redirect stdin

nohup $CMD >/dev/null & disown            # redirect log to null, continue, disown
```


<a name="readinginsideterminal"/>

---

##### Reading within Terminal


```bash
head -$NUM                                # show first $NUM lines

cat $FILE -n                              # show line numbers

more $FILE                                # start at top and scroll with spacebar 

less $FILE                                # load enough to fit screen -- load more dynamically
```

```bash
glow $MDFILE                              # glow app for reading md files in terminal
                                          # finds markdown files in current directory and below
                                          # if you’re in a Git repository, Glow will search the repo

# list hotkeys
? 

# read from stdin
glow -

# fetch README from github project
glow https://github.com/$URL

# fetch md file from HTTP
glow https://$URL

# set word wrap max to 60 characters
glow -w 60

# choose pager default is ANSI-aware less -r
glow -p

# custom JSON stylesheet
glow -s mystyle.json

# stash curr file
glow stash README.md   
```

```bash
# set custom pager
PAGER=
export PAGER
```

<div align="right" font-family="monospace">
    <b><a href="#Moderately">↥ Back To Top</a></b>
</div>

---


<a name="writinginsideterminal"/>

##### Writing within Terminal


<a name="vim"/>


```bash
vim $FILE                 # write with vim modal typing

nano $FILE                # write with nano hotkeys

emacs $FILE               # write with emacs hotkeys

echo $TEXT >> $FILE

cat [options|grep|sed] $TEXT >> $FILE
```



<a name="vimcheatsheet"/>

###### Vim Cheatsheet

- [cursor](#vimcursor)
- [cut & paste](#vimcutpaste)
- [insert](#viminsert)
- [editing](#vimediting)
- [visual](#vimvisual)
- [replace](#vimreplace)
- [indent](#vimindent)
- [registers](#vimregisters)
- [marks](#vimmarks)
- [macros](#vimmacros)
- [diff](#vimdiff)
- [window](#vimwindow)
- [tabs](#vimtabs)
- [exiting](#vimexiting)

<a name="vimcursor"/>

| **___CURSOR___**  | **____________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `K` | open man page for word under the cursor | `h` | move cursor left |
| `j` | move cursor down | `k` | move cursor up |
| `l` | move cursor right | `H` | move to top of screen |
| `M` | move to middle of screen | `L` | move to bottom of screen |
| `w` | jump forwards to the start of a word | `W` | jump forwards to the start of a word (words can contain punctuation) |
| `e` | jump forwards to the end of a word | `E` | jump forwards to the end of a word (words can contain punctuation) |
| `b` | jump backwards to the start of a word | `B` | jump backwards to the start of a word (words can contain punctuation) |
| `%` | move to matching character (default supported pairs: '()', '{}', '[]' - use <code>:h matchpairs</code> in vim for more info) | `0` | jump to the start of the line |
| `^` | jump to the first non-blank character of the line | `$` | jump to the end of the line |
| `g_` | jump to the last non-blank character of the line | `gg` | go to the first line of the document |
| `G` | go to the last line of the document | `5gg`  or `5G` | go to line 5 |
| `gd` | move to local declaration | `gD` | move to global declaration |
| `fx` | jump to next occurrence of character x | `tx` | jump to before next occurrence of character x |
| `Fx` | jump to previous occurence of character x | `Tx` | jump to after previous occurence of character x |
| `;` | repeat previous f, t, F or T movement | `,` | repeat previous f, t, F or T movement, backwards |
| `}` | jump to next paragraph (or function/block, when editing code) | `{` | jump to previous paragraph (or function/block, when editing code) |
| `zz` | center cursor on screen | `Ctrl`  + `e` | move screen down one line (without moving cursor) |
| `Ctrl`  + `y` | move screen up one line (without moving cursor) | `Ctrl`  + `b` | move back one full screen |
| `Ctrl`  + `f` | move forward one full screen | `Ctrl`  + `d` | move forward 1/2 a screen |
| `Ctrl`  + `u` | move back 1/2 a screen |


---


<a name="vimcutpaste"/>

| **___CUT PASTE___**  | **_____________________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `yy` | yank (copy) a line | `2yy` | yank (copy) 2 lines |
| `yw` | yank (copy) the characters of the word from the cursor position to the start of the next word | `y$` | yank (copy) to end of line |
| `p` | put (paste) the clipboard after cursor | `P` | put (paste) before cursor |
| `dd` | delete (cut) a line | `2dd` | delete (cut) 2 lines |
| `dw` | delete (cut) the characters of the word from the cursor position to the start of the next word | `D` | delete (cut) to the end of the line |
| `d$` | delete (cut) to the end of the line | `x` | delete (cut) character |


---


<a name="viminsert"/>

| **___INSERT MODE___**  | **_____________________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `i` | insert before the cursor | `I` | insert at the beginning of the line |
| `a` | insert (append) after the cursor | `A` | insert (append) at the end of the line |
| `o` | append (open) a new line below the current line | `O` | append (open) a new line above the current line |
| `ea` | insert (append) at the end of the word | `Ctrl`  + `h` | delete the character before the cursor during insert mode |
| `Ctrl`  + `w` | delete word before the cursor during insert mode | `Ctrl`  + `j` | begin new line during insert mode |
| `Ctrl`  + `t` | indent (move right) line one shiftwidth during insert mode | `Ctrl`  + `d` | de-indent (move left) line one shiftwidth during insert mode |
| `Ctrl`  + `n` | insert (auto-complete) next match before the cursor during insert mode | `Ctrl`  + `p` | insert (auto-complete) previous match before the cursor during insert mode |
| `Ctrl`  + `rx` | insert the contents of register x | `Esc` | exit insert mode |


---


<a name="vimediting"/>

| **___EDITING___**  | **____________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `r` | replace a single character | `J` | join line below to the current one with one space in between |
| `gJ` | join line below to the current one without space in between | `gwip` | reflow paragraph |
| `g~` | switch case up to motion | `gu` | change to lowercase up to motion |
| `gU` | change to uppercase up to motion | `cc` | change (replace) entire line |
| `C` | change (replace) to the end of the line | `c$` | change (replace) to the end of the line |
| `ciw` | change (replace) entire word | `cw` | change (replace) to the end of the word |
| `s` | delete character and substitute text | `S` | delete line and substitute text (same as cc) |
| `xp` | transpose two letters (delete and paste) | `u` | undo |
| `U` | restore (undo) last changed line | `Ctrl`  + `r` | redo |
| `.` | repeat last command |


---


<a name="vimvisual"/>

| **___VISUAL MODE___**  | **______________________________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `v` | start visual mode, mark lines, then do a command (like y-yank) | `V` | start linewise visual mode |
| `o` | move to other end of marked area | `Ctrl`  + `v` | start visual block mode |
| `O` | move to other corner of block | `aw` | mark a word |
| `ab` | a block with () | `aB` | a block with {} |
| `at` | a block with &lt;&gt; tags | `ib` | inner block with () |
| `iB` | inner block with {} | `it` | inner block with &lt;&gt; tags |
| `Esc` | exit visual mode | `U` | change marked text to uppercase |
| `&gt;` | shift text right | `&lt;` | shift text left |
| `y` | yank (copy) marked text | `d` | delete marked text |
| `~` | switch case | `u` | change marked text to lowercase |



---

<a name="vimreplace"/>

| **___SEARCH & REPLACE___**  | **_____________________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `/pattern` | search for pattern | `?pattern` | search backward for pattern |
| `\vpattern` | 'very magic' pattern: non-alphanumeric characters are interpreted as special regex symbols (no escaping needed) | `n` | repeat search in same direction |
| `N` | repeat search in opposite direction | `:%s/old/new/g` | replace all old with new throughout file |
| `:%s/old/new/gc` |  replace all old with new throughout file with confirmations | `:noh[lsearch]` | remove highlighting of search matches |
| `:cn[ext]` | jump to the next match | `:cp[revious]` | jump to the previous match |
| `:cope[n]` | open a window containing the list of matches | `:ccl[ose]` | close the quickfix window |


---

<a name="vimindent"/>

| **___INDENT___**  | **_____________________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `&gt;&gt;` | indent (move right) line one shiftwidth | `&lt;&lt;` | de-indent (move left) line one shiftwidth |
| `&gt;%` | indent a block with () or {} (cursor on brace) | `&gt;ib` | indent inner block with () |
| `&gt;at` | indent a block with &lt;&gt; tags | `3==` | re-indent 3 lines |
| `=%` | re-indent a block with () or {} (cursor on brace) | `=iB` | re-indent inner block with {} |
| `gg=G` | re-indent entire buffer | `]p` | paste and adjust indent to current line |



---

<a name="vimregisters"/>

| **___REGISTERS___**  | **_____________________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `:reg[isters]` | show registers content | `"xy` | yank into register x |
| `"xp` | paste contents of register x | `"+y` | yank into the system clipboard register |
| `"+p` | paste from the system clipboard register |
| `*` | clipboard contents (X11 primary)| `+` | clipboard contents (X11 clipboard)
| `/` | last search pattern| `:` | last command-line
| `.` | last inserted text| `-` | last small (less than a line) delete
| `=` | expression register |


<a name="vimmarks"/>


| **___MARKS___**  | **_____________________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `:marks` | list of marks | `ma` | set current position for mark A |
| ``a` | jump to position of mark A | `y`a` | yank text to position of mark A |
| ``0` | go to the position where Vim was previously exited | ``"` | go to the position when last editing this file |
| ``.` | go to the position of the last change in this file | ```` | go to the position before the last jump |
| `:ju[mps]` | list of jumps | `Ctrl`  + `i` | go to newer position in jump list |
| `Ctrl`  + `o` | go to older position in jump list | `:changes` | list of changes |
| `g,` | go to newer position in change list | `g;` | go to older position in change list |
| `Ctrl`  + `]` | jump to the tag under cursor |


---

<a name="vimmacros"/>

| **___MACROS___**  | **_____________________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `qa` | record macro a | `q` | stop recording macro |
| `@a` | run macro a | `@@` | rerun last run macro |


---

<a name="vimdiff"/>

| **___VIM DIFF___**  | **____________________________________** |  **______________**  | **______________________________** |
|:----:|:--------------------------------------|:----:|-------|
| `zf` | manually define a fold up to motion | `zd` | delete fold under the cursor |
| `za` | toggle fold under the cursor | `zo` | open fold under the cursor |
| `zc` | close fold under the cursor | `zr` | reduce (open) all folds by one level |
| `zm` | fold more (close) all folds by one level | `zi` | toggle folding functionality |
| `[c` | jump to start of previous change | `do` or `:diffg[et]` | obtain (get) difference (from other buffer) |
| `dp` or `:diffpu[t]` | put difference (to other buffer) | `:diffthis` | make current window part of diff |
| `:dif[fupdate]` | update differences | `:diffo[ff]` | switch off diff mode for current window |
| `]c` | jump to start of next change |

---

<a name="vimwindow"/>

| **___MULTIPLE FILES___**  | **_____________________________________** |  **______________**  | **______________________________** |
|-------|----|---|----|
| `:e[dit] file` | edit a file in a new buffer |  `Ctrl` + `wk` | move cursor to the window above (horizontal split) |
| `:bn[ext]` | go to the next buffer            | `:bp[revious]` | go to the previous buffer |
| `:bd[elete]` | delete a buffer (close a file)             | `:b[uffer]#` | go to a buffer by index # |
| `:b[uffer] file` | go to a buffer by file             | `:ls` or `:buffers` | list all open buffers |
| `:sp[lit] file` | open a file in a new buffer and split window             | `:vs[plit] file` | open a file in a new buffer and vertically split window |
| `:vert[ical] ba[ll]` | edit all buffers as vertical windows             | `:tab ba[ll]` | edit all buffers as tabs |
| `Ctrl` + `ws` | split window             | `Ctrl` + `wv` | split window vertically |
| `Ctrl` + `ww` | switch windows             | `Ctrl` + `wq` | quit a window |
| `Ctrl` + `wx` | exchange current window with next one             | `Ctrl` + `w=` | make all windows equal height &amp; width 
| `Ctrl` + `wh` | move cursor to the left window (vertical split)            |`Ctrl` + `wl` | move cursor to the right window (vertical split) | 
| `Ctrl` + `wj` | move cursor to the window below (horizontal split)             |


---

<a name="vimtabs"/>

| **___TABS___**  | **_________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `:tabnew` | `:tabnew {page.words.file}` | `Ctrl`  + `wT` | move the current split window into its own tab |
| `gt`  or `:tabn[ext]` | move to the next tab | `gT`  or `:tabp[revious]` | move to the previous tab |
| `#gt` | move to tab number # | `:tabm[ove] #` | move current tab to the #th position (indexed from 0) |
| `:tabc[lose]` | close the current tab and all its windows | `:tabo[nly]` | close all tabs except for the current one |
| `:tabdo` |command - run the <code>command</code> on all tabs (e.g. <code>:tabdo q</code> - closes all opened tabs) |


---

<a name="vimexiting"/>

| **___EXITING___**  | **_______________________________** |  **______________**  | **______________________________** |
|:----:|:-------|:----:|:-------|
| `:w` | write (save) the file, but don't exit | `:w !sudo tee %` | write out the current file using sudo |
| `:wq`  or `:x`  or `ZZ` | write (save) and quit | `:q` | quit (fails if there are unsaved changes) |
| `:q!`  or `ZQ` | quit and throw away unsaved changes | `:wqa` | write (save) and quit on all tabs |
| `:h[elp] keyword` | open help for keyword | `:sav[eas] file` | save file as |
| `:clo[se]` | close current pane | `:ter[minal]` | open a terminal window |




[from](https://github.com/rtorr/vim-cheat-sheet/blob/master/License.txt)


---


<a name="vimtips"/>


###### *More Vim Tips*

- Prefix a cursor movement command with a number to repeat it. For example, `4j` |moves down 4 lines

- When marking, instead of b or B one can also use ( or { respectively. 

- To jump to a mark you can either use a backtick (``</kbd>) or an apostrophe (`'</kbd>). Using an apostrophe jumps to the beginning (first non-black) of the line holding the mark

- The commands for folding (e.g. za) operate on one level. To operate on all levels, use uppercase letters (e.g. zA).

- To view the differences of files, one can directly start Vim in diff mode by running vimdiff in a terminal. One can even set this as git difftool.

- Registers are being stored in ~/.viminfo, and will be loaded again on next restart of vim.

<div align="right" font-family="monospace">
    <b><a href="#Moderately">↥ Back To Top</a></b>
</div>


---



<a name="nano"/>

<a name="nanocheatsheet"/>

###### Nano Cheatsheet

<table>
<thead><tr><th title="Field #1" align=center colspan=2>File handling</th>
<th align=center colspan=2 title="Field #3">Moving around</th>
<th align=center colspan=2 title="Field #5">Editing</th>
</tr></thead>
<tbody><tr>
<td>Ctrl+S </td>
<td>Save current file</td>
<td>Ctrl+B </td>
<td>One character backward</td>
<td>Ctrl+K </td>
<td>Cut current line into cutbuffer</td>
</tr>
<tr>
<td>Ctrl+O</td>
<td>Offer to write file (&quot;Save as&quot;)</td>
<td>Ctrl+F</td>
<td>One character forward</td>
<td>Alt+6</td>
<td>Copy current line into cutbuffer</td>
</tr>
<tr>
<td>Ctrl+R</td>
<td>Insert a file into current one</td>
<td>Ctrl+?</td>
<td>One word backward</td>
<td>Ctrl+U</td>
<td>Paste contents of cutbuffer</td>
</tr>
<tr>
<td>Ctrl+X</td>
<td>Close buffer, exit from nano</td>
<td>Ctrl+?</td>
<td>One word forward</td>
<td>Alt+T</td>
<td>Cut until end of buffer</td>
</tr>
<tr>
<td align=center colspan=2>Search and replace</td>
<td>Ctrl+A</td>
<td>To start of line</td>
<td>Ctrl+]</td>
<td>Complete current word</td>
</tr>
<tr>
<td>Ctrl+Q </td>
<td>Start backward search</td>
<td>Ctrl+E</td>
<td>To end of line</td>
<td>Alt+3</td>
<td>Comment/uncomment line/region</td>
</tr>
<tr>
<td>Ctrl+W</td>
<td>Start forward search</td>
<td>Ctrl+P</td>
<td>One line up</td>
<td>Alt+U</td>
<td>Undo last action</td>
</tr>
<tr>
<td>Alt+Q</td>
<td>Find next occurrence backward</td>
<td>Ctrl+N</td>
<td>One line down</td>
<td>Alt+E</td>
<td>Redo last undone action</td>
</tr>
<tr>
<td>Alt+W</td>
<td>Find next occurrence forward</td>
<td>Ctrl+?</td>
<td>To previous block</td>
<td align=center colspan=2>Information</td>
</tr>
<tr>
<td>Alt+R</td>
<td>Start a replacing session</td>
<td>Ctrl+?</td>
<td>To next block</td>
<td>Ctrl+C </td>
<td>Report cursor position</td>
</tr>
<tr>
<td align=center colspan=2>Deletion</td>
<td>Ctrl+Y</td>
<td>One page up</td>
<td>Alt+D</td>
<td>Report line/word/character count</td>
</tr>
<tr>
<td>Ctrl+H</td>
<td>Delete character before cursor </td>
<td>Ctrl+V</td>
<td>One page down</td>
<td>Ctrl+G</td>
<td>Display help text</td>
</tr>
<tr>
<td>Ctrl+D</td>
<td>Delete character under cursor</td>
<td>Alt+\</td>
<td>To top of buffer</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>Alt+Bsp</td>
<td>Delete word to the left</td>
<td>Alt+/</td>
<td>To end of buffer</td>
<td align=center colspan=2>Various</td>
</tr>
<tr>
<td>Ctrl+Del </td>
<td>Delete word to the right</td>
<td  align=center colspan=2> Special movement</td>
<td>Alt+A</td>
<td>Turn the mark on/off</td>
</tr>
<tr>
<td>Alt+Del</td>
<td>Delete current line</td>
<td>Alt+G </td>
<td>Go to specified line</td>
<td>Tab</td>
<td>Indent marked region</td>
</tr>
<tr>
<td align=center colspan=2>Operations</td>
<td>Alt+]</td>
<td>Go to complementary bracket</td>
<td>Shift+Tab </td>
<td>Unindent marked region</td>
</tr>
<tr>
<td>Ctrl+T </td>
<td>Execute some command</td>
<td>Alt+?</td>
<td>Scroll viewport up</td>
<td>Alt+N</td>
<td>Turn line numbers on/off</td>
</tr>
<tr>
<td>Ctrl+J</td>
<td>Justify paragraph or region</td>
<td>Alt+?</td>
<td>Scroll viewport down</td>
<td>Alt+P</td>
<td>Turn visible whitespace on/off</td>
</tr>
<tr>
<td>Alt+J</td>
<td>Justify entire buffer</td>
<td>Alt+&lt;</td>
<td>Switch to preceding buffer</td>
<td>Alt+V</td>
<td>Enter next keystroke verbatim</td>
</tr>
<tr>
<td>Alt+B</td>
<td>Run a syntax check</td>
<td>Alt+&gt;</td>
<td>Switch to succeeding buffer</td>
<td>Ctrl+L</td>
<td>Refresh the screen</td>
</tr>
<tr>
<td>Alt+F</td>
<td>Run a formatter/fixer/arranger</td>
<td>Ctrl+Z</td>
<td>Suspend nano</td>
</tr>
<tr>
<td>Alt+:</td>
<td>Start/stop recording of macro</td>
</tr>
<tr>
<td>Alt+;</td>
<td>Replay macro</td>
</tbody></table>


<a name="SometimesVery"/>


<div align="right" position="absolute" font-size=12 margin=0 opacity= .6 margin-right=0 margin-left=75%><a href="#table-of-contents">Very Top (目次)</a></div> 


![Pictures](bash-shell-usage.png)



# SOMETIMES VERY USEFUL


<a name="SometimesVery"/>


- [System Stats](#system_stat)
  - [internal](#internal_stats)
  - [network](#network_stats)
    - [*ifconfig*](#ifconfig)
    - [*netstat*](#netstat)
    - [*nmap*](#nmap)
  - [processes](#PID)
  - [killing processes](#killing)



<a name="system_stat"/>


#### System Stats

<a name="internal_stats"/>

###### Internal

```bash
top

free                  # free and used memory

uptime

atop

slabtop               # display kernel slab cache information in real time

vmstat                # virtual memory statistics

w                     # show who is logged on and what they are doing.
```



###### Controlling systemd System and Service Manager

```bash
systemctl $CMD $UNIT

sudo systemctl restart httpd


    list-units [PATTERN...]             List units currently in memory
    start UNIT...                       Start (activate) one or more units
    stop UNIT...                        Stop (deactivate) one or more units
    reload UNIT...                      Reload one or more units
    restart UNIT...                     Start or restart one or more units
    try-restart UNIT...                 Restart one or more units if active
    reload-or-restart UNIT...           Reload one or more units if possible,
    kill UNIT...                        Send signal to processes of a unit
    clean UNIT...                       Clean runtime, cache, state, logs or
                                        configuration of unit
    is-active PATTERN...                Check whether units are active
    is-failed PATTERN...                Check whether units are failed
    status [PATTERN...|PID...]          Show runtime status of one or more units
    show [PATTERN...|JOB...]            Show properties of one or more
                                        units/jobs or the manager
    cat PATTERN...                      Show files and drop-ins of specified units
    set-property UNIT PROPERTY=VALUE... Sets one or more properties of a unit
    help PATTERN...|PID...              Show manual for one or more units
```



<a name="network_stats"/>


 ###### Network

<a name="ifconfig"/>

 ```bash
 ifconfig

ifconfig [-a] [-v] [-s] <interface> [[<AF>] <address>]

      [add|del <address>[/<prefixlen>]]
      [[-]broadcast|pinpoint [<address>]]
      [netmask|dstaddr|tunnel <address>]
      [[-]trailers]  [[-]arp]  [[-]allmulti]
      [io_addr <NN>]  [media <type>]
      [up|down] ...
```

```bash
iwconfig                      # wireless
```

<a name="netstat"/>


```bash
netstat

netstat [-vWnNcaeol] [<Socket> ...]

      -r, --route              display routing table
      -i, --interfaces         display interface table
      -s, --statistics         display networking statistics (like SNMP)
      -M, --masquerade         display masqueraded connections
      -N, --symbolic           resolve hardware names
      -p, --programs           display PID/Program name for sockets
      -l, --listening          display listening server sockets
      -a, --all                display all sockets (default: connected)
      -F, --fib                display Forwarding Information Base (default)
      -Z, --context            display SELinux security context for sockets
```

<a name="nmap"/>


```bash
nmap

nmap [Scan Type(s)] [Options] {hostnames, IP addresses, networks, etc.}

nmap scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254

      -iL <inputfilename>: Input from list of hosts/networks
      -iR <num hosts>: Choose random targets
      --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
      --excludefile <exclude_file>: Exclude list from file

```

<a name="PID"/>

###### Find Process ID

```bash
top | grep $PROCESS

ps -ef | grep $PROCESS

htop --sort-key=PID

ps aux | grep $PROCESS
      
      -a = show proccesses for all users
      -u = display the processs user/owner
      -x = also show processes not attached to terminal

```

###### Snapshot of Process

```bash
ps

# process tree:
  ps -ejH
  ps axjf

# info about threads:
  ps -eLf
  ps axms

# security info:
  ps -eo euser,ruser,suser,fuser,f,comm,label
  ps axZ
  ps -eM

# see every process running as root (real & effective ID) in user format:
  ps -U root -u root u

# see every process with a user-defined format:
  ps -eo pid,tid,class,rtprio,ni,pri,psr,pcpu,stat,wchan:14,comm
  ps axo stat,euid,ruid,tty,tpgid,sess,pgrp,ppid,pid,pcpu,comm
  ps -Ao pid,tt,user,fname,tmout,f,wchan

# print only the process IDs of syslogd:
  ps -C syslogd -o pid=

# Print only the name of PID $NUM:
  ps -q $NUM -o comm=
```

<a name="killing"/>

###### Killing Processes


```bash
kill $PID

killall [process by name]

# signals
1 (hangup)
9 (kill signal)
15 (termination signal)
17 (stop process)

man 7 signal 

# firewall
sudo ufw | [disable] or [enable] | firewall

```

###### External System Monitor Apps

```bash
htop
ipcalc
bpytop [-b [cpu] [rem] [net] [proc]
iftop
sysstat
atop
iptraf
ipconfig      #  Windows
```


<a name="Sometimes"/>


<div align="right" position="absolute" font-size=12 margin=0 opacity= .6 margin-right=0 margin-left=75%><a href="#table-of-contents">Very Top (目次)</a></div>


![Pictures](bash-shell-usage.png)

 
# SOMETIMES USEFUL


<a name="Sometimes"/>


- [Compression](#Compression)
  - [extracting](#extracting)
  - [compressing](#compressing)


###### Unsigned repositories


```bash
sudo apt-add-repository -r
sudo apt-get update --allow-unauthenticated
``` 


<a name="Compression"/>

### Compression


###### Common Bash Commands for Zip Files


```bash
zipinfo $zipfile
zipgrep $zipfile
zcat 
zmore
zipdetails
```


###### Split Zip into Smaller Zip Files

```bash
zipslit $zipfile
```

###### Write Comments in Zipfile to stdout


```bash
zipnote $zipfile
```


-------------

<div align="right" font-family="monospace">
    <b><a href="#Sometimes">↥ Back To Top</a></b>
</div>


<a name="extracting"/>


#### Extract


```bash
uncompress $FILE               
unzip $FILE                    # list, test, and extract compressed files in archive
```


###### Tar


```bash
uz ~/*.gz                       # tar archive zipped w/ gzip like man pages
```

```bash
tar --extract $FILEgz           

tar --[append|create|diff|catenate|list|delete|update]

  -T, --files-from=FILE      get names to extract or create from FILE

  -O, --to-stdout            extract files to standard output
      --skip-old-files       dont replace existing files when extracting,
                             silently skip over them
      --to-command=COMMAND   pipe extracted files to another program
      --overwrite            overwrite existing files when extracting
```


###### Gzip'd 


```bash
gungzip
  -c, --stdout      write on standard output, keep original files unchanged
  -f, --force       force overwrite of output file and compress links
  -l, --list        list compressed file contents
  -r, --recursive   operate recursively on directories
  -t, --test        test compressed file integrity
  -v, --verbose     verbose mode
```

```bash
lz $ARCHIVE                     # gunzip and ls the archive
```


-------

<div align="right" font-family="monospace">
    <b><a href="#Sometimes">↥ Back To Top</a></b>
</div>


<a name="compressing"/>

#### Compress


###### Zip


```bash
compress $FILE
zforece $FILE                   # force gz extension
zip $dir
```


###### Tar ( gnu | oldgnu | pax | posix | ustar | v7 )


```bash
tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.
tar -tvf archive.tar         # List all files in archive.tar verbosely.
```

```bash
  -a, --auto-compress        use archive suffix to determine the compression
                             program
  -I, --use-compress-program=PROG
      --bzip2|xz|lzip|lzma|lzop|gzip|ztsd|compress
```

```bash
  -H, --format=FORMAT        create archive of the given format
  -f, --file=ARCHIVE         use archive file or device ARCHIVE
      --remove-files         remove files after adding them to the archive
      --recursion            recurse into directories (default)
  -A, --catenate, --concatenate   append tar files to an archive
  -c, --create               create a new archive
  -r, --append               append files to the end of an archive
  -u, --update               only append files newer than copy in archive
```


###### Gzip 


```bash
tgz $dir                     # make gzip'd tar archive
```


```bash
gzip $FILE
  -c, --stdout      write on standard output, keep original files unchanged
  -d, --decompress  decompress
  -f, --force       force overwrite of output file and compress links
  -k, --keep        keep (dont delete) input files
  -r, --recursive   operate recursively on directories
      --rsyncable   make rsync-friendly archive
  -S, --suffix=SUF  use suffix SUF on compressed files
  -t, --test        test compressed file integrity
  -1, --fast        compress faster
  -9, --best        compress better
```


<a name="kindof"/>


<div align="right" position="absolute" font-size=12 margin=0 opacity= .6 margin-right=0 margin-left=75%><a href="#table-of-contents">Very Top (目次)</a></div> 


![Pictures](bash-shell-usage.png)


# KIND OF USEFUL 🐷


<a name="contents-3"/>


- [Shell Prompts](#shell_prompts)


###### Show Directory Size


```bash
sudo du /$DIR|$FILE


    -h, --human-readable  print sizes in human readable format (e.g., 1K 234M 2G)
    -a, --all             write counts for all files, not just directories
    -c, --total           produce a grand total
    -d, --max-depth=N     print the total for a directory (or file, with --all)
                            only if it is N or fewer levels below the command
                            line argument;  --max-depth=0 is the same as
                            --summarize
    -S, --separate-dirs   for directories do not include size of subdirectories
    -s, --summarize       display only a total for each argument

    -t, --threshold=SIZE  exclude entries smaller than SIZE if positive,
                            or entries greater than SIZE if negative
        --time            show time of the last modification of any file in the
                            directory, or any of its subdirectories
        --time=WORD       show time as WORD instead of modification time:
                            atime, access, use, ctime or status
        --time-style=STYLE  show times using STYLE, which can be:
                              full-iso, long-iso, iso, or +FORMAT;
                              FORMAT is interpreted like in 'date'
        --exclude=PATTERN    exclude files that match PATTERN

```


<a name="shell_prompts"/>

#### Shell Prompts


###### Command Number (*to use with history expansion*)

```bash
\!$
```


###### Colorize Parts of Prompt

```bash
\e[                 # start color scheme.
x;y                 # color pair to use (x;y)
\e[m                # stop color scheme.
```


###### [***x;y Color Code System***](https://misc.flogisoft.com/bash/tip_colors_and_formatting)


###### Prompt Generators *(choose attributes and site auto-generates prompt)*


- [***Generator with Types of Info***](http://bashrcgenerator.com/) 
- [***Generator with Colors***](https://ezprompt.net/) 


###### More Options


| Characters | Prompt Addition |
|:-------:|:------- |
\a | an ASCII bell character (07)
\d | the date in “Weekday Month Date” format (e.g., “Tue May 26”)
\D{format} | the format is passed to strftime(3) and the result is inserted into the prompt string; an empty format results in a locale-specific time representation. The braces are required
\e | an ASCII escape character (033)
\h | the hostname up to the first ‘.’
\H | the hostname
\j | the number of jobs currently managed by the shell
\l | the basename of the shellâ€™s terminal device name
\n | newline
\r | carriage return
\s | the name of the shell, the basename of $0 (the portion following the final slash)
\t | the current time in 24-hour HH|MM|SS format
\T | the current time in 12-hour HH|MM|SS format
\@ | the current time in 12-hour am/pm format
\A | the current time in 24-hour HH|MM format
\u | the username of the current user
\v | the version of bash (e.g., 2.00)
\V | the release of bash, version + patch level (e.g., 2.00.0)
\w | the current working directory, with $HOME abbreviated with a tilde
\W | the basename of the current working directory, with $HOME abbreviated with a tilde
\! | the history number of this command
\# | the command number of this command
\$ | if the effective UID is 0, a #, otherwise a $
\nnn | the character corresponding to the octal number nnn
\\ | a backslash
\[ | begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt
\] | end a sequence of non-printing characters



###### Random Emoji Every Command

```bash
EMOJIS=(📼 🍀 😂 🤖 💣 🧸 🛍️  🈹 🈴 🈯 🈚 🈂️ 📟 🖱️  💻 🖥️  🔌 🔋\
 📠 🖲️  💾 🚬 🐶 🦧 🐺 🦊 🦝 🐈 🐅 🐆 🐷 🐖 🐗 🐏 🐪 🐘 🐼 🐨 🦇 \
 🐔 🦃 🐓 🐥 🐧 🐦 🦅 🦆 🦉 🐸 )


RANDOM_EMOJI() {
  SELECTED_EMOJI=${EMOJIS[$RANDOM % ${#EMOJIS[@]}]};
  echo $SELECTED_EMOJI;
}

export PS1='[\!][\[foo bar\]][\$(RANDOM_EMOJI)] '
```

###### ***NOTE:*** `\$(FUNCTION)` re-executes on every command -- `$(FUNCTION)` only on shell init

[List of Every Emoji 1.0](https://old.reddit.com/r/copypasta/comments/h9zrv5/list_of_every_single_emoji/)


###### Emoji Based on Exit Status

```bash
function success_indicator() {
    if [ $? -eq 0 ] ; then
        echo "?"
    else
        echo "?"
    fi
}

export PS1='\$(success_indicator) $ '
```

###### Cool Aliases

```bash
alias l="clear; ls -t -a --color=always; echo -e '\nCurrent Dir:               \e[2;94m'$(pwd -P)'\e[m';echo -e 'Total Space:               \e[1;96m'$(sudo du -hs)'\e[m'; echo -e 'File Count:                \e[1;96m'$(sudo du --inodes -s)' files\e[m\n'"
```
---

#### Footnotes

[A-Z Index of Commands](https://ss64.com/bash/)

  <div align="center" style="text-align: center; font-family: monospace; allign: center">
    Made with <g-emoji class="g-emoji" alias="heart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png">
  <img class="emoji" alt="heart" height="20" width="20" src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png"></g-emoji> <a href="https://www.bymyself.life">bymyself</a>
  </div>
  
<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div> 
