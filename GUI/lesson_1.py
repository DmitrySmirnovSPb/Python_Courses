from tkinter import *

root = Tk()
root.title('Новое окно программы')
root.resizable(False, False)

w = 800
h = 600

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = int(ws / 2 - w / 2)
y = int(hs / 2 - h / 2)

root.geometry('{0}x{1}+{2}+{3}'.format(w,h,x,y))

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

root.mainloop()
print('Окно закрыто')

newWindow = Tk()

startX = int(ws - wNW - 10)
startY = 0

print(ws)
print(hs)

newWindow.title('Новое окно ДЗ правый верхний')
newWindow.geometry('{0}x{1}+{2}+{3}'.format(wNW,hNW,startX,startY))

root.mainloop()