import webbrowser

d2l = "http://d2l.arizona.edu/d2l/home"
gradescope = "https://www.gradescope.com/"
piazza = "https://piazza.com/class/kjrt729oxxx51b"
webassign = "https://www.webassign.net/v4cgi/student.pl?v=20210130024728bafa2e74-fceb-4c52-8608-92e94d38206c_528562::app-254@arizona"
textbooks = "https://online.vitalsource.com/#/"
studentcenter = "https://uaccess.arizona.edu/"
gcal = "https://calendar.google.com/calendar/u/0/r?pli=1"
csc_cal = "https://benjdd.com/courses/cs110/spring-2021/schedule/"

chrome_path =  "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

webbrowser.get(chrome_path).open_new_tab(d2l)
webbrowser.get(chrome_path).open_new(gradescope)
webbrowser.get(chrome_path).open(piazza)
webbrowser.get(chrome_path).open(webassign)
webbrowser.get(chrome_path).open(textbooks)
webbrowser.get(chrome_path).open(studentcenter)
webbrowser.get(chrome_path).open(gcal)
webbrowser.get(chrome_path).open(csc_cal)