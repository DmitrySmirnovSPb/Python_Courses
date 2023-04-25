from tkinter import *
from setWindow import *

root = Tk()
setWindow(root)
lable= Label(root, text='Ваш любимый цвет')
lable.pack()

choice1 = StringVar()
choice1.set('green')
r1 = Radiobutton(root, text='Красный', variable=choice1, value='red')
r2 = Radiobutton(root, text='Зелёный', variable=choice1, value='green')
r3 = Radiobutton(root, text='Голубой', variable=choice1, value='blue')
r1.pack()
r2.pack()
r3.pack()

lable1= Label(root, text='Ваш любимый автомобиль')
lable1.pack()

choice2 = IntVar()
choice2.set(0)
r4 = Radiobutton(root, text='Запорожец', variable=choice2, value=0)
r5 = Radiobutton(root, text='Жигули', variable=choice2, value=1)
r6 = Radiobutton(root, text='Москвич', variable=choice2, value=2)
r4.pack()
r5.pack()
r6.pack()

root.mainloop()


print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

sityes = ('Moscow', 'Saint-Petersburg', 'London', 'Pekin', 'Kiev')
root = Tk()
setWindow(root)
lable= Label(root, text='Выбери город мечты')
lable.pack()
choice = IntVar()
for i in range(len(sityes)):
    Radiobutton(root, text=sityes[i], variable=choice, value=i).pack()
#    print(sityes[i])


root.mainloop()