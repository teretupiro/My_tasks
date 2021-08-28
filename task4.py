from tkinter import *

def replace(event):
    entry.get()
    l.insert(0,entry.get())

def rereplace(event):
    l.get(0)
    entry.insert(0,l.get(0))

root=Tk()
root.geometry('300x300')

entry=Entry()
entry.pack(side=BOTTOM)

l=Listbox()
l.pack()

entry.bind('<Return>',replace)
l.bind('<Double-Button-1>',rereplace)


root.mainloop()





