from tkinter import *
import random as RND
from setWindow import *

def handlerenter(event):
    event.widget.config(bg="red")

def handlerleave(event):
    event.widget.config(bg="yellow")

root = Tk()
setWindow(root)

button1 = Button(root, text="Кнопка 1", font="Tahoma 20", bg="yellow")
button2 = Button(root, text="Кнопка 2", font="Tahoma 20", bg="yellow")

button1.bind("<Enter>", handlerenter)
button1.bind("<Leave>", handlerleave)
button2.bind("<Enter>", handlerenter)
button2.bind("<Leave>", handlerleave)

button1.pack()
button2.pack()

root.mainloop()

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

color = ['red','green', 'yellow']

def Color(event):
    i = RND.randint(0,len(color) - 1)
    event.widget.config(bg=color[i])

def ColorStart(event):
    event.widget.config(bg='SystemButtonFace')


root = Tk()
setWindow(root)
print(root.cget('bg'))
root.bind("<Enter>", Color)
root.bind("<Leave>", ColorStart)

root.mainloop()