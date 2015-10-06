# -*- coding: utf8 -*-
from Tkinter import *
from ScrolledText import ScrolledText
import base64

root = Tk()

def doCount(s):
    s = s.replace("\n"," ")
    sl = s.split(" ")
    totalQ = 0
    total = 0
    q = False
    for x in range(0,len(sl)):
        i = sl[x].encode("utf-8")
        if not i == "":
            totalQ += 1
            #if not (u'“' in i and u'”' in i) or not i.count('"') == 2:
            if not (options["startChar"] in i and options["endChar"] in i):
                if options["startChar"] in i or options["endChar"] in i:
                    q = not q
                else:
                    if not q:total += 1

def openFile():
    pass#STUB

##BASE64 IMAGES
icon_settings_off_raw   = "R0lGODlhIAAgAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAgACAAAAiQAP8JHEiwoMGDCBMqXMjwHwAADSMKfPhQIkGKBilCLIgRocaNEz9e1Ojxo8mTIg+iXHkyIcuXIEvCNMlwZsuFN0emVEhT5U6ZHYFW9NlTaNCQOYkWdYiSZ1OdPzMmhTrUKM6oA5cajYmU5FWbXp2CPap0bFWpZrF2TXuWKtWYapGi5cqUbsOwFp3m3cu3b8GAADs="
icon_settings_on_raw    = "R0lGODlhIAAgAPcAAAAAAGZmZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAgACAAAAivAP8JHEiwoMGDCBMqXMjwHwAADSMKBBAgAESJAx9eJEjRokGNCTt6zFix4kaHJU9yLGlRI0uTLlMiFPmyps2RB2nevKny486dPX2+1BiTZdCCOnsmZUjzaNOFT0ManblUqlGVOk0qzIoTZc2jE21irTpzqNOpVrVuRStU7Vq2JOGWNUv0K9OfPKHiBZp2r9i5MB9+Ldp1pVuvh0WCBYn08MSHGOOCjZxxMuXLmBkGBAA7"
##BASE64 END
icon_settings_off       = PhotoImage(data=icon_settings_off_raw)
icon_settings_on        = PhotoImage(data=icon_settings_on_raw)




##VARIABLES
wwq = StringVar()#WORDS WITH QUOTES
wwq.set("0")

wwoq = StringVar()#WORDS WITHOUT QUOTES
wwoq.set("0")



##TOPBAR
topbarLeft = Frame(root)
topbarLeft.grid(row=0,column=0,sticky="w")
topbarMid = Frame(root)
topbarMid.grid(row=0,column=0)
topbarRight = Frame(root)
topbarRight.grid(row=0,column=0,sticky="e")

##TOPBARLEFT
#toggleCountB = Button(topbarLeft,height=2,command=toggleCount)
openB = Button(topbarLeft, height=2, command=openFile,text="Open",width=10)
openB.grid(row=0,column=1,padx=5,pady=5)


##TOPBARMID
twq = Frame(topbarMid)
twq.grid(row=0,column=0,sticky="e")

twql = Label(twq,text="With Quotes:")
twql.grid(row=0,column=0)

twqv = Label(twq,textvar=wwq)
twqv.grid(row=1,column=0)

Canvas(topbarMid,width=40,height=1).grid(row=0,column=1)


twoq = Frame(topbarMid)
twoq.grid(row=0,column=2,sticky="w")

twoql = Label(twoq,text="Without Quotes:")
twoql.grid(row=0,column=0)

twoqv = Label(twoq,textvar=wwoq)
twoqv.grid(row=1,column=0)


##TOPBARRIGHT

def destroyCheck():
    global settingsMenu
    options.config(image=icon_settings_off)
    settingsMenu.destroy()
    settingsMenu = None
    root.unbind("<Motion>")
        
def onMove(e):
    currentx = e.x_root
    currenty = e.y_root
    if (currentx > boundMenux[1]) or (currenty > boundMenuy[1]) or (currentx < boundMenux[0] and currenty > boundMenuy[0]) or (currentx < boundPathx and currenty < boundMenuy[0]):
        destroyCheck()
    
boundMenux = None
boundMenuy = None
boundPathx = None
def onSettingsEnter(e):
    global settingsMenu,boundMenux,boundMenuy,boundPathx,boundPathy
    if settingsMenu == None:
        options.config(image=icon_settings_on)
        root.bind("<Motion>",onMove)
        ##WINDOWVARS
        width = 300
        height = 400
        offsetx = options.winfo_rootx()-width+41
        offsety = options.winfo_rooty()+44
        boundMenux = [offsetx,offsetx+width]
        boundMenuy = [offsety,offsety+height]
        boundPathx = offsetx+width-41
        ##WINDOWVARS END
        top = Toplevel()
        top.geometry("{x}x{y}+{ox}+{oy}".format(x=width,y=height,ox=offsetx,oy=offsety))
        top.overrideredirect(1)
        Label(top,text="Hello World!").pack()
        settingsMenu = top



exitMenu = True
exitPath = True
settingsMenu = None

options = Label(topbarRight,image=icon_settings_off)
options.grid(row=0,column=999,padx=5,pady=5)
options.bind("<Enter>",onSettingsEnter)


main = ScrolledText(root,width=120,height=30)

main.grid(row=1,column=0)

root.mainloop()
