from tkinter import*

root=Tk()
root.geometry('500x500')

c=Canvas(root,width=500,height=500)
c.pack()

x=10
while x<480:
    c.create_arc(x, 500, x+10, 400,fill='green')
    x=x+10

c.create_rectangle(200,250,300,350,fill='blue')
c.create_polygon((200, 250), (250, 150), (300, 250))
c.create_oval(400, 10, 490, 90,fill='yellow')



root.mainloop()



