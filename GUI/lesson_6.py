from tkinter import *
from setWindow import *
import numpy as np
tmp = np.random.randint(2)
root = Tk()
setWindow(root)

choice = IntVar()

check = Checkbutton(root,bd=20, text='Согласие на обработку персональных данных', variable=choice, onvalue=1, offvalue=0)
print(tmp)
choice.set(tmp)
print(choice.get())

check.pack()

root.mainloop()

print(choice.get())

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

