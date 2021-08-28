from tkinter import *

def change(event):
    t['width']=entry1.get()
    t['height']=entry2.get()


def focus_in (event):
    event.widget['bg']='white'

def focus_out(event):
    event.widget['bg']='lightgrey'


root=Tk()
root.geometry('500x500')
root.bind('<Return>',change)

entry1=Entry()
entry1.place(x=180,y=0)

entry2=Entry()
entry2.place(x=180,y=30)


t=Text()
t.pack(side=BOTTOM)
t.bind('<FocusIn>',focus_in)
t.bind('<FocusOut>',focus_out)


b=Button(text='Change')
b.bind('<Button-1>',change)


b.place(x=320,y=0)



root.mainloop()