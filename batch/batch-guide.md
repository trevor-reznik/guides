
# Batch Guide

<a name="table-of-contents"/>

##### Table of Contents
- [**Commands**](#commands)
  - [***List of Commands***](#command-list)
  - [***Sleep***](#sleep-command)
  - [***Open Files/Apps***](#open)
- [**Interactive Usage**](#interactive-usage)
  - [**Navigating Directories**](#navigating)
- [**Scripts**](#scripts)
  - [**Send Keys**](#send-keys)
- [**Variables**](#variables)

-----------


<a name="commands"/>

## Commands


###### Reference Sheet

<a name="command-list"/>

| Command | Usage |
|:-------:|:---------------------------------------------------------------------------------|
|`   VER           `|   shows the version of MS-DOS you are using                                           |
|`   ASSOC         `|   that associates an extension with a file type (FTYPE), displays existing associations, or deletes an association   |
|`   CD            `|   helps in making changes to a different directory, or displays the current directory   |
|`   CLS           `|   clears the screen                                                                   |
|`   COPY          `|   is used for copying files from one location to the other                            |
|`   DEL           `|   deletes files and not directories                                                   |
|`   DIR           `|   lists the contents of a directory                                                   |
|`   DATE          `|   help to find the system date                                                        |
|`   ECHO          `|   displays messages, or turns command echoing on or off                               |
|`   EXIT          `|   exits the DOS console                                                               |
|`   MD            `|   creates a new directory in the current location                                     |
|`   MOVE          `|   moves files or directories between directories                                      |
|`   PATH          `|   displays or sets the path variable                                                  |
|`   PAUSE         `|   prompts the user and waits for a line of input to be entered                        |
|`   PROMPT        `|   can be used to change or reset the cmd.exe prompt                                   |
|`   RD            `|   removes directories, but the directories need to be empty before they can be removed   |
|`   REN           `|   Renames files and directories                                                                          |
|`   REM           `|   is used for remarks in batch files, preventing the content of the remark from being executed   |
|`   START         `|   starts a program in new window, or opens a document                                 |
|`   TIME          `|   sets or displays the time                                                           |
|`   TYPE          `|   prints the content of a file or files to the output                                 |
|`   VOL           `|   displays the volume labels                                                          |
|`   ATTRIB        `|   Displays or sets the attributes of the files in the curret directory                                   |
|`   CHKDSK        `|   checks the disk for any problems                                                    |
|`   CHOICE        `|   provides a list of options to the user                                              |
|`   CMD           `|   invokes another instance of command prompt                                          |
|`   COMP          `|   compares 2 files based on the file size                                             |
|`   CONVERT       `|   converts a volume from FAT16 or FAT32 file system to NTFS file system               |
|`   DRIVERQUERY   `|   shows all installed device drivers and their properties                             |
|`   EXPAND        `|   extracts files from compressed .cab cabinet files                                   |
|`   FIND          `|   searches for a string in files or input, outputting matching lines                  |
|`   FORMAT        `|   formats a disk to use Windows-supported file system such as FAT, FAT32 or NTFS, thereby overwriting the previous content of the disk   |
|`   HELP          `|   shows the list of Windows-supplied commands                                         |
|`   IPCONFIG      `|   displays Windows IP Configuration. Shows configuration by connection and the name of that connection   |
|`   LABEL         `|   adds, sets or removes a disk label                                                  |
|`   MORE          `|   displays the contents of a file or files, one screen at a time                      |
|`   NET           `|   Provides various network services, depending on the command used                                       |
|`   PING          `|   sends ICMP/IP "echo" packets over the network to the designated address             |
|`   SHUTDOWN      `|   shuts down a computer, or logs off the current user                                 |
|`   SORT          `|   takes the input from a source file and sorts its contents alphabetically, from A to Z or Z to A. It prints the output on the console   |
|`   SUBST         `|   assigns a drive letter to a local folder, displays current assignments, or removes an assignment   |
|`   SYSTEMINFO    `|   shows configuration of a computer and its operating system                          |
|`   TASKKILL      `|   ends one or more tasks                                                              |
|`   TASKLIST      `|   lists tasks, including task name and process id (PID)                               |
|`   XCOPY         `|   copies files and directories in a more advanced way                                 |
|`   TREE          `|   displays a tree of all subdirectories of the current directory to any level of recursion or depth   |
|`   FC            `|   lists the actual differences between two files                                      |
|`   DISKPART      `|   shows and configures the properties of disk partitions                              |
|`   TITLE         `|   sets the title displayed in the console window                                      |


-----


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>





<a name="sleep-command"/>

#### Sleep

```PowerShell
timeout /t 30
```


The timeout would get interrupted if the user hits any key; however, the command also accepts the optional switch /nobreak, which effectively ignores anything the user may press, except an explicit CTRL-C:

```PowerShell
timeout /t 30 /nobreak
```

Additionally, if you don't want the command to print its countdown on the screen, you can redirect its output to NUL:

```PowerShell
timeout /t 30 /nobreak > NUL
```


<a name="open"/>

#### Open Files/Apps


```PowerShell
START application_here "c:\path to file to open\foo.dat"
```


-----


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>





<a name="interactive-usage"/>

## Interactice Usage


<a name="navigating"/>

#### Navigating Directories


###### Return to Previous Directory

```PowerShell
popd

pushd D:\a
```

###### Get most recent file in directory

```Powershell
# for loop. Set variable 
for /f "tokens=*" %%a in ('dir /b /od') do set newest=%%a

With %newest% defined

    (1) copy and delete: 

# copy newest file by referencing the %newest% variable
copy "%newest%" D:\b

# return to login directory
Popd

    (2) Or open: 

# echo a string that references %newest% by the file’s name
echo "Finished Downloading  >>  %newest%"

# open file using START and the absolute path
START C:\Users\12064\Videos\wget_downloads\"%most_recent_download_in_wgetVideo_folder%"

# set the working directory back to login directory so the directory is not 
# still in the current one when the script terminates
pushd C:\Users\12064
```


-----


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>



<a name="scripts"/>

## Scripts




<a name="send-keys"/>


#### Send Keys

Reference [1](https://stackoverflow.com/questions/22836457/how-to-make-a-batch-file-to-run-a-hotkey) [2](https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/windows-scripting/8c6yea83(v=vs.84)?redirectedfrom=MSDN )


1. create python script or use WshShell.Run to start app
2. call script or use WshShell.Run 
3. delay
4. AppActivate the window
5. WshShell.SendKeys
6. Create Batch file 
  a. wscript “scripename.vbs”



-----


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>



<a name="variables"/>

## Variables

Refer to variables with `%variable%`

```PowerShell
Set A/ [arithmetic here]
```


