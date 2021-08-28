from tkinter import *



def openfile():
    s = entry.get()
    print(s)
    f=open(s,'r')
    text.insert(1.0,f.read())
    f.close()

def savefile():
    s = entry.get()
    print(s)
    f = open(s, 'w')
    g=text.get(1.0,END)
    f.write(g)
    f.close()




root = Tk()
root.geometry('500x500')

text = Text(width=50, height=50)
text.place(x=0, y=50)

entry = Entry(width=50)
entry.place(x=0, y=0)

btnop = Button(text='Открыть', width=10, height=2, command=openfile)
btnop.place(x=300, y=0)

btnsv = Button(text='Сохранить', width=10, height=2,command=savefile)
btnsv.place(x=400, y=0)

root.mainloop()
