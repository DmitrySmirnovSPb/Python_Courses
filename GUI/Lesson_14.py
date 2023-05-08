from tkinter import *
from setWindow import *

root = Tk()
setWindow(root)

photo = PhotoImage(file="test.png")
bgimage = photo.zoom(2, 3)

bg = Label(root, image=bgimage)

buttonimage = photo.subsample(4, 4)
button = Button(root, image=buttonimage)

bg.place(x=0, y=0, relwidth=1, relheight=1)

button.pack()

root.mainloop()

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

link = input('Введите адрес изображения: ')
z = float(input('Введите масштаб: '))

root = Tk()
setWindow(root)
try:
    photo = PhotoImage(file=link)

    if z < 1 and z > 0 :
        mas = int(1 / z)
        img = photo.subsample(mas, mas)
        bg = Label(root, image=img)
    elif z >= 1:
        z = int(z)
        img = photo.zoom(z,z)
        bg = Label(root, image=img)
    else:
        bg = Label(root, text='Вы ввели не корректный масштаб.')
except TclError:
    bg = Label(root, text='Ошибка открытия изображения', font='Arial 20')

bg.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()