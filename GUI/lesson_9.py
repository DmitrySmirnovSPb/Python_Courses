from tkinter import *
from setWindow import *

root = Tk()
setWindow(root)

data = ('Moscow', 'Saint-Petersburg', 'London', 'Pekin', 'Kiev')

list = Listbox(root, width=20, height=4, font='Tahoma 20', selectmode=MULTIPLE)# selectmode=SINGLE

for d in data:
    list.insert(END, d)
list.selection_set(0,1)
print(list.selection_get())

indexes = list.curselection()
print(indexes)


list.pack()

root.mainloop()


print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

sityes = []

while True:
    temp = input('Введите название города или 0 для выхода: ')
    print()
    if temp == '0' and len(sityes) > 0:
        break
    if temp != '0' and temp != '':
        sityes.append(temp)

root = Tk()
setWindow(root)
list = Listbox(root, width=20, height=4, font='Tahoma 20', selectmode=SINGLE)

for d in sityes:
    list.insert(END, d)

list.pack()

root.mainloop()