import os
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import *

# the window
root = Tk()
root.geometry('500x600')
root.config(bg='black')
root.title('Untitled -IDE')

# setting file variable
file = None

# our commands


def openFile():
    global file
    file = askopenfilename(title='open a file - Notepad',initialdir='/',filetypes=(('text files','*.txt'),("PY files",'.py'),('All files','*.*')))
    if file == '':
        showinfo("Error","Please open a file")
    else:
        root.title(os.path.basename(file)+' -IDE')
        filet = open(file,'r')
        filee = filet.read()
        text.delete(1.0,END)
        text.insert(1.0,filee)
        filet.close()

def saveFile():
    if file==None:
        fiol = asksaveasfilename(filetypes=(('text files','*.txt'),('PY files','*.py'),('All files','*.*')))
        if fiol=='':
            showinfo("Error","Please give a file")
        else:
            fio = open(fiol,'w')
            fio.write(text.get(1.0,END))
            fio.close()
    else:
        fiol = open(file,'w')
        fiol.write(text.get(1.0,END))
        fiol.close()

def runfilelocal():
    if file == None:
        fiol = open('runnnning.py','w')
        fiol.write(text.get(1.0,END))
        fiol.close()
        os.system('runnnning.py')
    else:
        fiol = open(file,'w')
        fiol.write(text.get(1.0,END))
        fiol.close()
        os.system(f"\"{file}\"")

# our components
frame = Frame(
    root,
    bg='black'
) 
text = Text(
    root,
    bg="#002",
    wrap=WORD,
    foreground='cyan',
    font=("consolas",12,'BOLD'.lower()),
    insertbackground="white"
)
btn1 = Button(
    frame,
    fg='white',
    bg='#000000',
    text='open',
    command=openFile
)
btn2 = Button(
    frame,
    fg='white',
    text='save',
    bg='#000000',
    command=saveFile
)
btn3 = Button(
    frame,
    fg='white',
    bg='#000000',
    text='About',
    command=lambda:showinfo('About','Created by ratul Banerjee')
)
btn4 = Button(
    frame,
    fg='white',
    bg='#000000',
    text='Run',
    command=runfilelocal
)
btn5 = Button(
    frame,
    bg='#000000',
    fg='white',
    text='exit',
    command=lambda:root.destroy()
)


# packing the components
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=LEFT)
btn5.pack(side=LEFT)
frame.pack(anchor='nw',padx=5,pady=5)
text.pack(expand=True,fill=BOTH)


# adding syntax highlight
cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#002'}

# These five lines are optional. If omitted, default colours are used.
cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#002'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#002'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#002'}
cdg.tagdefs['STRING'] = {'foreground': 'yellow', 'background': '#002'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#002'}

ip.Percolator(text).insertfilter(cdg)

root.mainloop()