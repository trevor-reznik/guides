###
### Summer 2021 Homework Session Startup Script
### Christian P. Byrne
###


import webbrowser, os


csc120 = {
    "zoom" : "https://arizona.zoom.us/j/83314574912",
    "lectures" : r"https://arizona.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx?embedded=1#folderID=%22fd9b3d40-9629-4fea-991e-ad2100398613%22",
    "piazza" : "https://piazza.com/arizona/summer2021/csc120/",
    "d2l announcements" : "https://d2l.arizona.edu/d2l/lms/news/main.d2l?ou=1031117",
    "assignments" : "https://d2l.arizona.edu/d2l/le/content/1031117/Home",
    "syllabus" : "https://lecturer-russ.appspot.com/classes/cs120/summer21/120_Syllabus_Summer_21.pdf",
    "style guide" : "https://lecturer-russ.appspot.com/classes/cs120/summer21/style/pgm-style.html",
    "activities" : "https://lecturer-russ.appspot.com/classes/cs120/summer21/",
    "discord" : "https://discord.gg/axeUBqe9g5",
    "office hours" : "https://docs.google.com/spreadsheets/d/1p2Y8QvgvTzT5cvSpXf7Av0EG5zjQNPjsgJLJUOVNN6Q/edit?usp=sharing",
}

csc337 = {
    "syllabus" : "https://benjdd.com/courses/cs337/summer-2021/syllabus/index.html",
    "schedule" : "https://benjdd.com/courses/cs337/summer-2021/schedule/",
    "style guide" : "https://benjdd.com/courses/cs337/summer-2021/style/",
    "assignments" : "https://benjdd.com/courses/cs337/summer-2021/pas/",
    "playposit" : "https://d2l.arizona.edu/d2l/le/content/1039612/Home"
}

always = {
    "websites" : {
        "gradescope" : "https://www.gradescope.com/",
    },
    "applications" : {
        "placeholder" : False
    }
}


def csc120_session():
    for _ in ["lectures", "piazza", "d2l announcements", "assignments", "activities"]:
       webbrowser.open(csc120[_])     


def csc337_session():
    for _ in csc337.values(): webbrowser.open(_)     


if __name__ == "__main__":
    import sys
    print("Commands:\n[337] [120] [all]\n[{}]\n[{}]".format(
        "] [".join(csc120.keys()),
        "] [".join(csc337.keys())
    ), "\n\n\n"
    )
    if len(sys.argv) > 1:
        if "337" in sys.argv[1]: csc337_session()
        elif "120" in sys.argv[1]: csc120_session()
        elif "all" in sys.argv[1]:
            csc337_session()
            for _ in csc120.values(): webbrowser.open(_)
        else:
            webbrowser.open(csc337[sys.argv[1]]) if sys.argv[1] in csc337.keys() \
                else csc120[sys.argv[1]] if sys.argv[1] in csc120.keys() \
                    else exit()
    else:
        csc337_session()
        csc120_session()

    for _ in always["websites"].values(): webbrowser.open(_)
    os.chdir("/home/bymyself/school")
    for _ in ["ls -R", "code ."]: os.system(_)