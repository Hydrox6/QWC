from Tkinter import *
from ScrolledText import ScrolledText


def doCount():
    pass#STUB

def openFile():
    pass#STUB

def swapspace(widgetL,widgetV,stringvar,text):
    widgetL["text"] = text
    widgetV["textvariable"] = stringvar
    

root = Tk()

##VARIABLES
wwq = StringVar()#WORDS WITH QUOTES
wwq.set("0")
cwq = StringVar()#CHARACTERS WITH QUOTES (SPACES)
cwq.set("0")
cwqn = StringVar()#CHARACTERS WITH QUOTES (NO SPACES)
cwqn.set("1")

wwoq = StringVar()#WORDS WITHOUT QUOTES
wwoq.set("0")
cwoq = StringVar()#CHARACTERS WITHOUT QUOTES (SPACES)
cwoq.set("0")
cwoqn = StringVar()#CHARACTERS WITHOUT QUOTES (NO SPACES)
cwoqn.set("1")


##TOPBAR
topbarLeft = Frame(root)
topbarLeft.grid(row=0,column=0,sticky="w")
topbarMid = Frame(root)
topbarMid.grid(row=0,column=0)
topbarRight = Frame(root)
topbarRight.grid(row=0,column=0,sticky="e")

##TOPBARLEFT
openB = Button(topbarLeft, height=2, command=openFile,text="Open",width=10)
openB.grid(row=0,column=0,padx=5,pady=5)

##TOPBARMID
totalwq = Frame(topbarMid)
totalwq.grid(row=0,column=0,sticky="w")
totalwqL = Label(totalwq,text="Total With Quotes")
totalwqL.grid(row=0,column=0,columnspan=2)

twordswqL = Label(totalwq,text="Words: ")
twordswqL.grid(row=1,column=0)

twordswqV = Label(totalwq,textvar=wwq)
twordswqV.grid(row=1,column=1)

tcharswqL = Label(totalwq,text="Chars (w/ spaces): ")
tcharswqL.grid(row=2,column=0)


tcharswqV = Label(totalwq,textvar=cwq)
tcharswqV.grid(row=2,column=1)
tcharswqL.bind("<Enter>", lambda e,text="Without Spaces: ",wL=tcharswqL,wV=tcharswqV,v=cwqn: swapspace(wL,wV,v,text))
tcharswqL.bind("<Leave>", lambda e,text="Chars (w/ spaces): ",wL=tcharswqL,wV=tcharswqV,v=cwq: swapspace(wL,wV,v,text))

totalwoq = Frame(topbarMid)
totalwoq.grid(row=0,column=3,sticky="e")
totalwoqL = Label(totalwoq,text="Total Without Quotes")
totalwoqL.grid(row=0,column=0,columnspan=2)

twordswoqL = Label(totalwoq,text="Words: ")
twordswoqL.grid(row=1,column=0)

twordswoqV = Label(totalwoq,textvar=wwoq)
twordswoqV.grid(row=1,column=1)

tcharswoqL = Label(totalwoq,text="Chars (w/ spaces): ")
tcharswoqL.grid(row=2,column=0)


tcharswoqV = Label(totalwq,textvar=cwoq)
tcharswoqV.grid(row=2,column=1)
tcharswoqL.bind("<Enter>", lambda e,text="Without Spaces: ",wL=tcharswoqL,wV=tcharswoqV,v=cwoqn: swapspace(wL,wV,v,text))
tcharswoqL.bind("<Leave>", lambda e,text="Chars (w/ spaces): ",wL=tcharswoqL,wV=tcharswoqV,v=cwoq: swapspace(wL,wV,v,text))
##TOPBARRIGHT


main = ScrolledText(root,width=120,height=30)

main.grid(row=1,column=0)

root.mainloop()
