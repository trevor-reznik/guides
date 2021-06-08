set WshShell = WScript.CreateObject("WScript.Shell")
WScript.Sleep(2000)
WshShell.AppActivate "chrome"
WScript.Sleep(1000)
WshShell.SendKeys("^n")
WScript.Sleep(1000)
WshShell.Run "C:\Users\12064\batch_scripts\Math125\math_websites.py"
WScript.Sleep(3200)
WshShell.SendKeys("^1")
WScript.Sleep(1000)
WshShell.SendKeys("^w")
WScript.Sleep(1000)