![Banner](banners/guides.png)


<a name="table-of-contents"/>

 - [Plugin Managers](#Manager)
 - [Table Mode](#Mode)
 - [Notes](#Notes)
 - [Color Scheme Selector](#Selector)
 - [Python Mode](#PMode)
 - [Auto Comment](#Comment)
 - [Git ](#Git)
 - [Auto-Tag HTML](#HTML)
 - [File Explorer](#Explorer)
 - [Custom Indent Characters](#Characters)

---

<a name="Managers"/>


# Plugin Manager

```bash
# in .vimrc
Plugin $GITHUB_LINK 

# from shell
vim +PluginInstall +qall
vim +PluginUpdate +qall

# from vim shell
:PluginList
:PluginInstall
:PluginUpdate
```

<a name="Mode"/>

# Table Mode

```bash
:TableModeToggle
```
###### Usage

 1. `||` or `__` to being table mode while in INSERT mode
 2. `|` to delimit columns inbetween text
 3. `||` = horizontal lines between rows

###### [More](https://github.com/dhruvasagar/vim-table-mode)
 - Formatting existing content into a table
 - Moving around
 - Manipulating Table
 - Spreadsheet Capabilities
 - Formula Expressions


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

---


<a name="Notes"/>


# Notes 

###### Usage
```bash
:Note                           # create a new buffer and load the appropriate file type and syntax

:Note anything                  # edit a note containing anything in its title 
                                # (if none found, new created)

:DeleteNote                     # delete the current note

:SearchNotes $KEYWORD 

:RecentNotes                    # lists your notes by modification date
```

###### Folding / Lists

The vim-notes syntax uses atx-style headers just like Markdown markdown (one to six # marks at the start of the line) and supports text folding based on these headers. This allows easy navigation within notes that contain large (and possibly nested) sections of text separated by headers. 

###### [More](https://github.com/xolox/vim-notes)


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

---



<a name="Selector"/>

# Color Scheme Changer

###### Favorites

 - sonokai 
 - dogrun
 - solarized8_low
 - (base16-dracula)
 - space-vim-dark
 - spacecamp

###### Usage

```bash
:NextColorScheme                        # or Shift-F8
:RandomColorScheme                      # or Ctrl-F8
:PrevColorScheme
```


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

---


<a name="PMode"/>

# Python Mode


###### Usage

```bash
:help pymode
 
let g:
      pymode                                # Turn on
      (<leader>r)                           # Run Code
      (<leader>b)                           # Add/remove breakpoints 
      (:PymodeLint)                         # Run multiple code checkers simultaneously 
      (:PymodeLintAuto)                     # Autofix PEP8 errors 
      (<leader>K)                           # Search in python documentation 
      (<C-c>g)                              # Go to definition 
      pymode_warnings                       # Turn off warnings
      pymode_paths                          # Add value to sys path
      pymode_trim_whitespaces               # Trim unused white spaces on save
      pymode_options                        # Options
      pymode =0                             # Turn off

# Python motions & operators 
(]], 3[[, ]]M, vaC, viM, daC, ciM, ...)
```

###### Features

- Virtualenv support
- Improved Python folding
- Code refactoring
- Intellisense code-completion

###### [More](https://github.com/python-mode/python-mode)



<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

---


<a name="Comment"/>

# Auto Comments


```bash
gcc						>>  comment out a line (takes a count)
gc 						>>  comment out the target of a motion 
<!-- (for example, gcap to comment out a paragraph) --> 
gc visual mode  		>>  comment out the selection
gc operatorpending mode >>  target a comment
```

```bash
:7,17Commentary         # comment a range like 
:g/TODO/Commentary      # :global invocation
```



<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

---


<a name="Git"/>

# GitHub 


```bash
:Git                    # calls any arbitrary Git command 
```
###### [More](https://github.com/tpope/vim-fugitive)


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

---



<a name="HTML"/>

# Auto-Tag HTML

###### Usage

```bash
# After typing something:
<C-E>   # format tag                    
<C-n>   # cycle through empty elements. 
```

###### Keymappings

`div#header` expands to:

```html
    <div id="header"></div>
```

`div.align-left#header` expands to:

```html
    <div id="header" class="align-left"></div>
```

`div#header` + `div#footer` expands to:

```html
    <div id="header"></div>
    <div id="footer"></div>
```

`#menu > ul` expands to:

```html
    <div id="menu">
        <ul></ul>
    </div>
```

`#menu > h3` + `ul` expands to:

```html
    <div id="menu">
        <h3></h3>
        <ul></ul>
    </div>
```

`#header > h1{Welcome to our site}` expands to:

```html
    <div id="header">
        <h1>Welcome to our site</h1>
    </div>
```

`a[href=index.html]{Home}` expands to:

```html
    <a href="index.html">Home</a>
```

`ul > li*3` expands to:

```html
    <ul>
        <li></li>
        <li></li>
        <li></li>
    </ul>
```

`ul > li.item-$*3` expands to:


```html
    <ul>
        <li class="item-1"></li>
        <li class="item-2"></li>
        <li class="item-3"></li>
    </ul>
```
    
`ul > li.item-$*3 > strong` expands to:

```html
    <ul>
        <li class="item-1"><strong></strong></li>
        <li class="item-2"><strong></strong></li>
        <li class="item-3"><strong></strong></li>
    </ul>
```

`table > tr*2 > td.name + td*3` expands to:

```html
    <table>
        <tr>
            <td class="name"></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="name"></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </table>
```

`#header > ul > li < p{Footer}` expands to:

```html
    <!-- The < symbol goes back up the parent; i.e., the opposite of >. -->
    <div id="header">
        <ul>
            <li></li>
        </ul>
        <p>Footer</p>
    </div>
```

---

###### Emmet Usage

Type ("_" is the cursor position):

Then type `<c-y>`

Type the abbreviation as `div>p#foo$*3>a` 

and type `<c-y>`

Wrap with an Abbreviation Write as below.

```
  test1
  test2
  test3
```

Then do visual select(line wise) and type `<c-y>`  

Once you get to the `Tag:` prompt, type `ul>li*`

```html
  <ul>
      <li>test1</li>
      <li>test2</li>
      <li>test3</li>
  </ul>
```

If you type a tag, such as 'blockquote', then you'll see the following:

```html
  <blockquote>
      test1
      test2
      test3
  </blockquote>
```


3. **Balance a Tag Inward**

  type `<c-y>d` in insert mode.

4. **Balance a Tag Outward**

  type `<c-y>D` in insert mode.

5. **Go to the Next Edit Point**

  type `<c-y>n` in insert mode.

6. **Go to the Previous Edit Point**

  type `<c-y>N` in insert mode.

7. **Update an <img>’s Size**

  Move cursor to the img tag.

```html
  <img src="foo.png" />
```

Type `<c-y>i` on img tag

```html
  <img src="foo.png" width="32" height="48" />
```

8. **Merge Lines**

  select the lines, which include `<li>`

```html
  <ul>
  	<li class="list1"></li>
  	<li class="list2"></li>
  	<li class="list3"></li>
  </ul>
```
and then type `<c-y>m`

```html
  <ul>
  	<li class="list1"></li><li class="list2"></li><li class="list3"></li>
  </ul>
```

9. **Remove a Tag**

  Move cursor in block

```html  
  <div class="foo">
  	<a>cursor is here</a>
  </div>
```

  Type `<c-y>k` in insert mode.

```html
  <div class="foo">

  </div>
```

And type `<c-y>k` in there again.  


 10. **Split/Join Tag**

Move the cursor inside block

```html
  <div class="foo">
  	cursor is here
  </div>
```


Type `<c-y>j` in insert mode.

```html
  <div class="foo"/>
```

And then type `<c-y>j` in there again.

```html
  <div class="foo">
  </div>
```

---

###### ***Customize key mappings in vim/README.txt***

###### [More](https://raw.githubusercontent.com/mattn/emmet-vim/master/TUTORIAL)



<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

---


<a name="Explorer"/>


# File Explorer *(Command-t)* 

###### Functions

 - Opening files and buffers
 - Jumping to tags and help
 - Running commands, or previous searches and commands

###### Usage

```bash
# Bring up the Command-T file window
<Leader>t  			
:CommandT
  
# Enter relative or absoute path: 
:CommandT ../path/to/other/files

# Brings up the Command-T search window
:CommandTSearch   
```

###### Narrow Selection

Type letters in the prompt to narrow down the selection, showing only the files whose paths contain those letters in the specified order. 

Letters do not need to appear consecutively in a path in order for it to be classified as a match.

```bash
<CR>        open the selected file
<C-CR>      open the selected file in a new split window
<C-s>       open the selected file in a new split window
<C-v>       open the selected file in a new vertical split window
<C-t>       open the selected file in a new tab
<C-d>       delete the selected buffer
<C-j>       select next file in the file listing
<C-n>       select next file in the file listing
<Down>      select next file in the file listing
<C-k>       select previous file in the file listing
<C-p>       select previous file in the file listing
<Up>        select previous file in the file listing
<C-f>       flush the cache (see |:CommandTFlush| for details)
<C-q>       place the current matches in the quickfix window
<C-c>       cancel (dismisses file listing)
```

###### [More](https://github.com/wincent/command-t/blob/master/doc/command-t.txt)



<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

---


<a name="Characters"/>

   
# Indentation Queues / Markers         

###### Usage

```bash
:IndentLinesToggle                                  # toggles lines on and off.
```

###### Change Character Color

```bash
let g:indentLine_setColors = 120
let g:indentLine_color_term = 1effbc
let g:indentLine_color_tty_light = 7 " (default: 4)
let g:indentLine_color_dark = 1 " (default: 2)
let g:indentLine_bgcolor_term = 202
let g:indentLine_bgcolor_gui = '#FF5F00'
```

###### Change Indentation Character

```bash
let g:indentLine_char = 'c'
```

###### Change Conceal Behavior


This plugin enables the Vim conceal feature which automatically hides stretches of text based on syntax highlighting. This setting will apply to all syntax items.
For example, users utilizing the built in json.vim syntax file will no longer see quotation marks in their JSON files.
indentLine will overwrite your "concealcursor" and "conceallevel" with default value:

```bash
let g:indentLine_concealcursor = 'inc'
let g:indentLine_conceallevel = 2
```

You can customize these settings, but the plugin will not function if conceallevel is not set to 1 or 2.
If you want to keep your conceal setting, put this line to your vim dotfile:

```bash
let g:indentLine_setConceal = 0
```

See the VIM Reference Manual for more information on the conceal feature.

----

  <div align="center" style="text-align: center; font-family: monospace; allign: center">
    Made with <g-emoji class="g-emoji" alias="heart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png">
  <img class="emoji" alt="heart" height="20" width="20" src="https://github.githubassets.com/images/icons/emoji/unicode/2764.png"></g-emoji> <a href="https://www.bymyself.life">bymyself</a>
  </div>


<div align="center" style="font-size: 11px; margin: 0; opacity:.6"><a href="#table-of-contents">Top (目次)</a></div> 
