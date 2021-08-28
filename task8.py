from tkinter import *
import  time



root = Tk()
root.geometry('1920x1080')

c = Canvas(root, width=1920, height=1080,
           bg="white")
c.pack()
ball = c.create_oval(0, 0, 100, 100, fill='black')

def getxy(event):
 getx=event.x_root
 gety=event.y_root
 print('x ',getx)
 print('y ',gety)
 c.coords(ball,getx-100,gety-100,getx+100,gety+100)






root.bind('<Button-1>',getxy)



root.mainloop()