https://www.itprotoday.com/powershell/powershell-why-youll-never-go-back-cmdexe-batch-files 
To create a PowerShell script, you simply create a text file, with a .ps1 extension, that contains the commands you want to execute. The commands in the script can be PowerShell cmdlets, batch files, PowerShell aliases, PowerShell functions, or anything else that you could type at a PowerShell prompt as a command to execute.
Consider the batch file (Sample1.cmd) and PowerShell script (Sample1.ps1) shown in Figure 1. These two scripts are functionally identical and will produce the exact same output. Note that the batch file uses replaceable parameters (%1 and %2) to mean “the first two parameters on the script’s command line.” Rather than replaceable parameters, PowerShell uses the Param statement to define its parameters. (The line breaks after the opening parenthesis of the Param statement and before its closing parenthesis are optional; I included them to improve readability.)
Run
Navigate to the directory where the script lives
PS> cd C:\my_path\yada_yada\ (enter)
Execute the script:
PS> .\run_import_script.ps1 (enter)
Script Running Policy – Admin Access
As an Administrator, you can set the execution policy by typing this into your PowerShell window:
Set-ExecutionPolicy RemoteSigned
For more information, see Using the Set-ExecutionPolicy Cmdlet.
When you are done, you can set the policy back to its default value with:
Set-ExecutionPolicy Restricted
Or:
You can bypass this policy for a single file by adding -ExecutionPolicy Bypass when running PowerShell
powershell -ExecutionPolicy Bypass -File script.ps1
