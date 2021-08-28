from tkinter import *

root=Tk()
root.geometry('200x150')

def change():
   if var.get() ==0:
       l['text']='1'
   elif var.get()==1:
       l['text']='2'
   elif var.get() == 2:
       l['text'] = '3'

var=IntVar()
var.set(0)

l=Label()
l.place(x=110,y=60)

frbtn=Radiobutton(text='1',variable=var,value=0,indicatoron=0,command=change)
frbtn.place(x=0,y=0)
srbtn=Radiobutton(text='2',variable=var,value=1,indicatoron=0,command=change)
srbtn.place(x=0,y=50)
trbtn=Radiobutton(text='3',variable=var,value=2,indicatoron=0,command=change)
trbtn.place(x=0,y=100)

root.mainloop()