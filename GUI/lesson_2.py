from tkinter import *
from setWindow import *
import numpy as np

root = Tk()
setWindow(root)

label = Label(root, text='Моя метка', font='HondaC 18', bg='#bbb', fg='#fff')

label.pack()

root.mainloop()

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

newWindow = Tk()

wNW = 1000
hNW = 500
startX = 0
startY = 0
newWindow.title('Новое окно ДЗ левый верхний')
newWindow.geometry('{0}x{1}+{2}+{3}'.format(wNW,hNW,startX,startY))

text = str(np.random.randint(1,1000))

label = Label(newWindow, text=text, font='Verdana 52', bg='#000', fg='red')

label.pack()

root.mainloop()