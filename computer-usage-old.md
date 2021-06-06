<!-- ________Recently Used________ -->


info [add-apt-repository] [apt-get] [wget]

info apt-secure
(trying to fix signing of repository)

info wget
(learning about wget)



<!-- ________Learning Journal________ -->



______________________________________________________________________


______________________________________________________________________
<u Trying to find out how to copy man pages for wget to my notes>

    [1] man -k copy
    [2] info cp
    [3] info wget --where
            (show location of man page for wget)
            >> /usr/share/info/wget.info.gz
    [4] man -k zip
            (finding the function for cat-ing a gz file)
    [5] man -k zip | grep print
    [6] man -k zip | grep page
            (filtering zip related commands for cat-like function)
    [7] info | grep zip
            (using info + grep because can't find the function)
            >> zmore: (gzip)Overview
    [8] zmore ../../usr/share/info/wget.info.gz
            (more'ing the man page to check if correct)
    [9] (release zmore will not be good for piping output)
    [1]	man -k gzip
            (searching for a cat function for zipped fileS)
    [2] info zcat
            (trying "zmore" but replacing more with cat)
            >> it exists
    [3] zcat ../../usr/share/info/wget.info.gz
            (works)
    [4] zcat ../../usr/share/info/wget.info.gz > temp.txt; gedit temp.txt
            (cat the zipped file, redirect to temp.txt, open temp.txt)



______________________________________________________________________
<u How can I redirect to my clipboard? >

    [1] man -k clipboard
        >> xclipboard
    [2] man xclipboard
        >> it is a program with a GUI
    [3] info xclipboard
        >> xclipboard [ -toolkitoption ... ] [ -w ] [ -nw ]
    [4] info xclipboard | grep SEE ALSO
        >> only printed the line that the word occurred
    [5] grep --help
        (finding how to control lines before/after)
    [6] info xclipboard | grep SEE ALSO -A 3
        (print three lines after) 
        >> X(7), xcutsel(1), xterm(1), 
            individual client documentation for how to make 
            a selection and send it to the CLIPBOARD.
    [7] man xcutsel
    [8] Better to Google this, found clipboard-cli program
    [9] it says it is installed through npm
    [1] apt-cache search clipboard
    [2] apt-cahce search clipboard | grep GTK --exclude=xfce
        (excluding for xfce desktops)
    [3] Just going to use npm
        info npm
        npm --help
        npm install -g clipboard-cli
    [4] forget permissions
        sudo npm install -g clipboard-cli
    [5] cd; nano .bashrc -> alias cb=clipboard
        
    
    
    
    
# HOTKEYS

| **Command**	  |	  **Function**  |
|:--------------- | ---------------:|
|`  ctrl shift x `|       save screenshot  |
|`  windows M    `|notification tray toggle|
|`  [ctrl shift s] `|       screenshot 2 clip|
` windows arrow`|    snap focused program|
|`  alt return   `|           open terminal|
|`  alt F7       `|   select window to move|
|`  windows L    `|             lock screen|
|`  alt space    `|     menu of focused app|
|`  windows D    `|           show desktop |
|`  windows H    `|         minimize window|
|`  windows A    `|           applications |
|`  ctrl H       `|      see hidden folders|
|`  ctrl L       `|      select address bar|
    
    
    
    
======================
# CUSTOM COMMANDS



| Command |Purpose | 
|:-------:|:------- |
vimnew				|new notepad on dekstop
xikinew				|xiki
nautilus [file]		|open with default program
notes 				|notes file in vim
glow [md file]		|markdown reading
f5					|run practice.py
comp [desktopfile]	|wait for pase -> diff	
writepy [f]			|editing env [fullscreen]
functions			|built-in python functions
roughcutpy [name]	|pract as [name] to desktop
q [#]				|random quote with number
a1 [program]		|nohup without writing log file
guide | open guides in glow
guides				|guides folder
guide				|MD guides in glow
desktop				|open desktop folder
how [guide name]	|open guide
pypractice			|practice.py in vim
naut [file]			|nautilus ~\[location]
vim ~/.imwheelrc	| change mouse scroll settings
setalias			|open bash.rc
scripts				|open scripts folder
vimrc |open vim config file
naut 				|explorer
web					|open firefox
deepin-config		|deepin config file
term4 [f]			|4 window term [fullscreen]
term				|open custom term 


======================
# CUSTOMIZATION COMMANDS



| Change Highlight Color | 
(1) open dconf-editor 
(2) go to path: org => gnome => desktop => interface
(3) gtk-color-scheme
(4) edit this part: selected_bg_color:#023C88
(5) IN CHROME: use "color highlight" chrome extension

| Command |Purpose | 
|:-------:|:------- |
wallpapers			|terminal_wallpapers
loops				|loops folder
megashots			|megashots folder
dconf-editor 		|-> /org/gnome/desktop/interface/
bg [pic/loop/vid]	|set terminology bg
gnome-tweaks 		|open tweaks
plank --preferences |plank taskbar settings
./config/autostart	|choose onstart apps
conky | (use theme manager)
komerabi(1) | create wallpaper
komerabi(2)| sudo cp -r [newbg] /System/Resources/Komorebi
komerabi(3)| cd /System/Resources/Komorebi; 
komerabi(4)|cd [wallpaper folder]; sudo mv thumb.jpg wallpaper.jpg



# WINDOWS CUSTOM COMMANDS


| Command | Purpose | 
|:-------:|:----:|
cntrl+shift+~		|		open Terminus
bymyself			|		School Material
vim					|		Open vim
money				|		bank,btc,coinbase,sessionbuddy
log					|		log in commands
soft				|		soft login start
wqchrome			|		save session in session buddy and exit chrome
chromesesh			|		open last session from chrome
anime				|		open latest crunchyroll page
gmails.py			|		All Emails
wgetsong			|		quick youtube-dl current URL with no args
coolors				|		coolors saved templates
school.py			|		All School Websites
gmails.py			|		All Emails
chromehistory.py	|		Open chrome -> history
sessionbuddy.py		|		open sessionbuddy
roshes.py			|		roshes  playlissts  w/ chrome ext
run1.py				|		porn hub + xvideos login
run.py				|		porn super log in
resources |
stackitup |
progress |
movies |
mesocycles |
fashion |
diet |
biohacking |


# RESEARCH

https://github.com/awesome-lists/awesome-bash
https://www.quora.com/What-is-the-most-useful-bash-script-that-you-have-ever-written
https://opensource.com/article/20/1/bash-scripts-aliases
https://linuxhint.com/30_bash_script_examples/
https://ostechnix.com/collection-useful-bash-scripts-heavy-commandline-users/
https://dev.to/aviaryan/some-helpful-bash-scripts-i-use-daily-40bd
https://www.8base.com/blog/the-simplest-productivity-hack-using-a-bash-script



