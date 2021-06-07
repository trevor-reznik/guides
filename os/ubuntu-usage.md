
# Windows Usage - Hotkeys, Aliases, etc.


<a name="table-of-contents"/>

##### Table of Contents

- [Ubuntu](#ubuntu)
  - [*hotkeys*](#hotkeys-ubuntu)
  - [*customization commands*](#customization-ubuntu)
- [Custom Aliases in some of my Bash profiles](#custom-aliases)




-------------------




<a name="hotkeys-ubuntu"/>

##### Hotkeys
    
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


<a name="customization-ubuntu"/>

##### Customization Commands

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


##### Change Highlight Color 

- In GTK Desktop:
  - dconf-editor 
  - path: org => gnome => desktop => interface
  - gtk-color-scheme
  - edit this part: `selected_bg_color:#023C88`
- In Chrome
  - use [color highlight](https://chrome.google.com/webstore/detail/highlight-color/dllbflhpdeinobodaaibnojmgejkkjii?hl=en) extension


<a name="custom-aliases"/>

## Custom Bash Aliases


| Command |Purpose | 
|:-------:|:------- |
`vimnew				` |open vim notepad from dekstop
`xikinew			` | new xiki notepad
`notes 				` | open presistent notes.txt file in vim
`f5					` |run `practice.py` file
`comp [desktopfile]	` |wait for paste -> run diff analysis	
`writepy [f]		` | a terminal editing env [fullscreen]
`functions			` | view list of built-in python functions
`roughcutpy [name]	` | save `practice.py` file as new file with [name] on dekstop
`q [#]				` | random quote [number in list]
`a1 [program]		` | `$a1=nohup >/dev/null $1 & disown`
`guide              ` | open guides directory viewer through glow gui
`guides				` | open guides folder using nautilus
`desktop			` | open desktop folder with nautilus
`how [guide name]	` | `$how=xdg-open $1-guide.txt`
`pypractice			` | open/edit `practice.py` in vim
`naut [file]		` | `$naut=nautilus ~\$1`
`vim ~/.imwheelrc	` | change mouse scroll settings
`setalias			` | open bash.rc w/ vim instead of nano
`scripts			` | open python-scripts folder w/ nautilus
`vimrc              ` | open vim config file with gedit
`naut 				` | `$naut=nautilus nohup >/dev/null & disown`
`web				` | `$web=google-chrome nohup >/dev/null & disown`
`deepin-config		` | open deepin config file with gedit
`term4 [f]			` | split deepin-terminnal into 2x2 [fullscreen]
`term				` | open custom deepin-terminal layout 

