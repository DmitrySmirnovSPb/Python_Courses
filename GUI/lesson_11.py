from tkinter import *
from setWindow import *

root = Tk()
setWindow(root)

lable1 = Label(root, text='Метка 1', font='Tahoma 20', bg='red', fg='#fff')
lable2 = Label(root, text='Метка 2', font='Tahoma 20', bg='green', fg='#fff')
lable3 = Label(root, text='Метка 3', font='Tahoma 20', bg='blue', fg='#fff')
lable4 = Label(root, text='Метка 4', font='Tahoma 20', bg='#123456', fg='#fff')
lable5 = Label(root, text='Метка 5', font='Tahoma 20', bg='#654321', fg='#fff')

lable1.pack(side='left',fill=X, expand=True, anchor='s') # s, w, e, n  -  возможные значения якаря (anchor)
lable2.pack(side='right')
lable3.pack(side='top')
lable4.pack(side='bottom')
lable5.pack(side='bottom')

root.mainloop()


print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')
root = Tk()
setWindow(root)

lable1 = Label(root, text='Метка 1', font='Tahoma 20', bg='red', fg='#fff', width=10, height=2)
lable2 = Label(root, text='Метка 2', font='Tahoma 20', bg='green', fg='#fff', width=10, height=2)
lable3 = Label(root, text='Метка 3', font='Tahoma 20', bg='blue', fg='#fff', width=10, height=2)
lable4 = Label(root, text='Метка 4', font='Tahoma 20', bg='#123456', fg='#fff', width=10, height=2)

lable1.pack(side='top')
lable2.pack(side='left', anchor='n')
lable3.pack(side='right', anchor='n')
lable4.pack(side='bottom')

root.mainloop()