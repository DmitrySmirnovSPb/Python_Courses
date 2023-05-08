from tkinter import *
import random as RND
from setWindow import *

root = Tk()
setWindow(root)


def handlerclick1(args):
    print(args)

def handlerclick2():
    print("Нажата кнопка")

def handlerclick3(event):
    print("Кликнули правой кнопкой мыши по кнопке: ")
    print(event.widget.cget('text'))

def handlerroot(event):
    print(event)
    print("Сработало событие")

button1 = Button(root, text="Кнопка 1", font="Tahoma 20", command=lambda: handlerclick1("Кнопка 1"))
button2 = Button(root, text="Кнопка 2", font="Tahoma 20", command=handlerclick2)
button3 = Button(root, text="Кнопка 3", font="Tahoma 20")

handler = button2.bind("<Button-3>", handlerclick3)
button3.bind("<Button-3>", handlerclick3)

button2.unbind(handlerclick3, handler)

root.bind("a", handlerroot)
root.bind("<Control-c>", handlerroot)

button1.pack()
button2.pack()
button3.pack()

root.mainloop()

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

def getRND(event=False):
    number = RND.randint(1,100)
    lb.config(text=number)

root = Tk()
setWindow(root)

button = Button(root, text='Сгенерировать случайное число', font="Tahoma 12", command=getRND)
lb = Label(root, font='Tahoma 20')

button.pack()
lb.pack()

root.mainloop()