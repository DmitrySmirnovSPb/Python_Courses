from tkinter import *
from setWindow import *
import numpy as np

root = Tk()
setWindow(root)

entry1 = Entry(root, font='Verdana 20', bg='#ddd', fg='green', bd=1)
entry2 = Entry(root, font='Verdana 20', bg='#ddd', fg='green', bd=1, show='%')
entry1.insert(END, 'Hello')
entry1.insert(END, 'ABC')

print(entry1.cget('font'))
print(entry1['font'])

entry1.pack()
entry2.pack()

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

entry = Entry(newWindow, font='Verdana 18', bg='#ddd', fg='green', bd=1)
text = input('Введите текст: ')
entry.insert(END, text)
entry.pack()
newWindow.mainloop()