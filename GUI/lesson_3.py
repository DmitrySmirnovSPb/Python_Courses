from tkinter import *
from setWindow import *

root = Tk()
setWindow(root)

label = Label(root, text='Моя метка', font='HondaC 18', bg='#bbb', fg='#fff')
label.pack()

button1 = Button(root, text='Нажми меня', font='HondaC 18', bg='#bbb', fg='#fff')
button1.pack()

button2 = Button(root, text='Нажми меня тоже', font='Tahoma 12', bg='#0f0', fg='#f00')
button2.pack()

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

text = 'str(np.random.randint(1,1000))'
label = Label(newWindow, text=text, font='Verdana 12')
label.grid(row=0, column=1)

button = Button(newWindow, text='Нажми меня', font='HondaC 18', bg='#bbb', fg='#fff')

button.grid(row=1, column=0)

root.mainloop()