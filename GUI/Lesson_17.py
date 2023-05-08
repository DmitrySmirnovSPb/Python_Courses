from tkinter import *
from setWindow import *

def handlerbutton(event=False):
    global en1
    global en2
    global display
    if event:
        print(event)
    try:
        r = str(float(en1.get()) + float(en2.get()))
        display.config(text="Сумма чисел равна: " + r)
    except ValueError:
        if not en1.get() or not en2.get():
            display.config(text="Вы ничего не ввели!")
        else:
            display.config(text="Вы ввели не числа!")

root = Tk()
setWindow(root)

header = Label(root, text="Суммирование чисел", font="Tahoma 20")
en1 = Entry(root, font="Tahoma 20")
en2 = Entry(root, font="Tahoma 20")

button = Button(root, text="Сумма", font="Tahoma 20", command=handlerbutton)
display = Label(root, font="Tahoma 20")

en1.bind("<Return>", handlerbutton)
en2.bind("<Return>", handlerbutton)

header.place(relx=0.5, rely=0.01, anchor="n")
en1.place(relx=0.5, rely=0.1, anchor="n")
en2.place(relx=0.5, rely=0.2, anchor="n")
button.place(relx=0.5, rely=0.3, anchor="n")
display.place(relx=0.5, rely=0.4, anchor="n")

root.mainloop()

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

def solvingTheQuadraticEquation(event=False):
    try:
        A =float(a.get())
        B =float(b.get())
        C =float(c.get())
        D =B*B-4*A*C
        txt = 'D = ' + str(D)
        if D < 0:
            txt = txt + '\nНет корней'
        elif A == 0:
            x = - C / B
            txt = 'x = ' + str(x)
        else:
            x1 = (-B + D**.5) / 2 / A
            x2 = (-B - D**.5) / 2 / A
            txt = txt + '\n x1 = ' + str(x1) + '\nx2 = ' + str(x2)
    except ValueError:
        if not a.get() or not b.get() or not c.get():
            txt = 'Вы ничего не ввели!'
        else:
            txt = 'Вы ввели не числа!'
    display.config(text=txt)
root = Tk()
setWindow(root)

frame = Frame(root)

header = Label(frame, text="ax^2 + bx + c = 0", font="Tahoma 20")
textA = Label(frame, text="a =", font="Tahoma 20")
textB = Label(frame, text="b =", font="Tahoma 20")
textC = Label(frame, text="c =", font="Tahoma 20")
a = Entry(frame, font="Tahoma 20")
b = Entry(frame, font="Tahoma 20")
c = Entry(frame, font="Tahoma 20")

button = Button(frame, text="Вычислить корни уравнения", font="Tahoma 20", command=solvingTheQuadraticEquation)
display = Label(frame, font="Tahoma 20")

a.bind("<Return>", solvingTheQuadraticEquation)
b.bind("<Return>", solvingTheQuadraticEquation)
c.bind("<Return>", solvingTheQuadraticEquation)
button.bind("<Return>", solvingTheQuadraticEquation)

frame.pack()
header.grid(row=0, column=0, columnspan=2)
textA.grid(row=1, column=0)
textB.grid(row=2, column=0)
textC.grid(row=3, column=0)
a.grid(row=1, column=1)
b.grid(row=2, column=1)
c.grid(row=3, column=1)
button.grid(row=4, column=0, columnspan=2)
display.grid(row=5, column=0, columnspan=2)

root.mainloop()