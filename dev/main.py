import downloader
import SearchList
import sys
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import scrolledtext

config = {}
def ref_plulist():
    print("plugins list on refreshing")
    downloader.download("https://github.com/SteveTaizhou/StevePyLibManager-Pro/blob/main/plugins/list.txt", "pluginslist.txt")
    print("plugins list refreshed")

def editconfig(op,value):
    config[op] = value
    with open("config.txt", "w") as configfile:
        keys = list(config.keys())
        values = list(config.values())
        for a in range(len(values)):
            configfile.write(str(keys[a]))
            configfile.write(",")
            configfile.write(str(values[a]))
            configfile.write("\n")
def output(*values, sep=' ',end='\n',file=sys.stdout,flush=False):
    logfile=open("log.txt", mode = "a")
    logfile.write(str(datetime.now())+"\n")
    for i in range(len(values)):
        if i!=0:
            logfile.write(str(sep))
        logfile.write(str(values[i]))
    logfile.write(end)
    logfile.close()
sys_stdout_write_real = sys.stdout.write
sys.stdout.write = output
#print(value, sep=' ',end='\n',file=sys.stdout,flush=False)
with open("config.txt", "r") as configfile:
    for linetext in configfile:
        linetextlist = linetext.split(",")
        config[linetextlist[0]] = linetextlist[1].strip()

language=config["language"]
del linetext
del linetextlist
def text(a):
    global language
    b={"cn":["库管理器", "StevePyLibManager Pro", "警告", "你真的想要退出吗？"],
       "en":["LibManager", "StevePyLibManager Pro", "Warning", "Do you really want to quit?"]}
    return b[language][a]

main_win=Tk()
main_win.title(text(1))
libman_win=Tk()
libman_win.title(text(0))
def mainclose():
    global config
    a=True
    if config["closewindowcheck"]=="1":
        a=messagebox.askokcancel(text(2), text(3))
    if a:
        print("exit")
        main_win.destroy()
        sys.exit(0)

def libmanshow():
    libman_win.deiconify()

libman_win.withdraw()
libman_win.protocol("WM_DELETE_WINDOW", libman_win.withdraw)
main_win.protocol("WM_DELETE_WINDOW", mainclose)
libmanbutton=Button(main_win, text=text(0), command = libmanshow)

libmanbutton.grid(column = 1,row = 1)
print(config)

editconfig("closewindowcheck", "0")
ref_plulist()


print("HelloWorld")
libman_win.mainloop()
