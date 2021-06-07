
[Docs](code.visualstudio.com/docs/cpp/config-linux)

## 1. Configure Build Task	
	
##### 1.  terminal > 

##### 2.  configure default build task > 

##### 3.  C/C++: g++ build active file > 

##### 4.  Creates tasks.json

## 2. tasks.json
 
```json
{
	"version": "2.0.0",
	"tasks": [
		{
			"type": "cppbuild",
			"label": "vanilla",
			"command": "/bin/g++",
			"args": [
				"-g",
				"${file}",
				"-o",
				"${fileDirname}/${fileBasenameNoExtension}"
			],
			"options": {
				"cwd": "${workspaceFolder}"
			},
			"problemMatcher": [
				"$gcc"
			],
			"group": {
				"kind": "build",
				"isDefault": true
			},
			"detail": "compiler: /bin/g++"
		}
	]
}
```

##### 1.  command setting 

specifies the program to run; in this case that is g++. 

##### 2.  args array 


specifies the * command-line arguments that will be passed to g++. 


These arguments must be specified in the order expected by the * compiler.


task tells g++ to take the active file (${file}), compile it, 


and create an executable file in the current * directory (${fileDirname}) 


with the same name as the active file but without an extension ($* {fileBasenameNoExtension}),


resulting in helloworld for our example.

##### 3.  label

is what you will see in the tasks list; you can name this whatever you like.

##### 4.  "isDefault"

true value in the group object specifies that this task will be run when 

you press Ctrl+Shift+B. This property is for convenience only; 

if you set it to false, you can still run it from the Terminal 

menu * with Tasks: Run Build Task.
 
## 3. Run
	  
##### 1.  Ctrl+Shift+B or from the Terminal main menu choose Run Build Task.
  
##### 2.  When the task starts, you should see the Integrated Terminal panel appear 

below the source code editor. 

##### 3.  After * the task completes, the terminal shows output from the compiler that 
	
indicates whether the build succeeded or failed.

##### 4.  Create a new terminal using the + button and you'll have a terminal running 

your default shell with the helloworld folder as the working directory. 

Run ls and you should now see the executable helloworld (no file * extension).
 
##### 5. You can run $your-program$ in the terminal by typing ./$your-program$
 
## 4. Modifying tasks.json

##### 1.  You can modify your tasks.json to build multiple C++ files by using an 

argument like "${workspaceFolder}/*.cpp" * instead of ${file}. 

##### 2.  You can also modify the output filename by replacing

"${fileDirname}/${fileBasenameNoExtension}* " with a hard-coded filename 

(for example 'helloworld.out')
 
## 5. Debug F5 Config

##### 1.  Run > Add Configuration

##### 2.  choose C++ (GDB/LLDB) > 

##### 3.  g++ build and debug active file > 

##### 4.  VS Code creates * a launch.json file, 

opens it in the editor, and builds and runs 'helloworld'.
 
## 6. launch.json

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++ - Build and debug active file",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}/${fileBasenameNoExtension}",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "vanilla",
            "miDebuggerPath": "/bin/gdb"
        }
    ]
}
```

##### 1.  program

specifies the program you want to debug. 

Here it is set to the active file folder $* {fileDirname}

and active filename without an extension ${fileBasenameNoExtension}, 

which if helloworld.cpp is the * active file will be helloworld.
 
##### 2.  By default, the C++ extension won't add any breakpoints to your source code

and the stopAtEntry value is set to * false.

Change the stopAtEntry value to true to cause the debugger to stop on

the main method when you start debugging.

## 7. Debugging

##### 1.  Press F5 or from the main menu choose Run > Start Debugging

##### 2.  The Integrated Terminal appears at the bottom of the source code editor. 

In the Debug Output tab, you see output * that indicates the 

debugger is up and running.

##### 3.  The editor highlights the first statement in the main method. 

This is a breakpoint that the C++ extension * automatically sets for you:

##### 4.  watch

To keep track of the value of a variable as your program executes, set a watch on the variable.



-------------------


### Troubleshooting


##### Compiler and linking errors

The most common cause of errors (such as undefined _main, or attempting to link with file built for

unknown-unsupported file format, and so on) occurs when helloworld.cpp is not the active file when

you start a * build or start debugging. This is because the compiler is trying to compile something

that isn't source code, like * your launch.json, tasks.json, or c_cpp_properties.json file.
 

##### Custom Configurations
 
###### C/C++ configurations#
If you want more control over the C/C++ extension, you can create a c_cpp_properties.json file, 
which will allow you to change settings such as the path to the compiler, include paths,
C++ standard (default is C++17), and more.

You can view the C/C++ configuration UI by running the command C/C++: Edit Configurations (UI) from
the Command * Palette (Ctrl+Shift+P).

This opens the C/C++ Configurations page. When you make changes here,
VS Code writes them to a file called * c_cpp_properties.json in the .vscode folder.

You only need to modify the Include path setting if your program includes
header files that are not in your * workspace or in the standard library path.

Visual Studio Code places these settings in .vscode/c_cpp_properties.json.
If you open that file directly, it * should look something like this:
  
###### Reusing your C++ configuration#

VS Code is now configured to use gcc on Linux. The configuration applies to 

the current workspace.

To reuse the * configuration, just copy the JSON files to a .vscode folder in a

new project folder (workspace) and change the * names of the source file(s) and executable as needed.

 
