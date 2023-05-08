from tkinter import *
from setWindow import *

root = Tk()
setWindow(root)

lable1 = Label(root, text='Метка 1', font='Tahoma 20', bg='red', fg='#fff')
lable2 = Label(root, text='Метка 2', font='Tahoma 20', bg='green', fg='#fff')
lable3 = Label(root, text='Метка 3', font='Tahoma 20', bg='blue', fg='#fff')
lable4 = Label(root, text='Метка 4', font='Tahoma 20', bg='#123456', fg='#fff')
lable5 = Label(root, text='Метка 5', font='Tahoma 20', bg='#654321', fg='#fff')

lable1.place(x=10, y=0)
'''
возможные значения  anchor
n, s, e, w
ne, nw, sw,se
center 
'''
lable2.place(relx=.5, rely=.5, anchor='center')
lable3.place(relx=.5, y=0, anchor='n')
lable4.place(relx=.5, rely=0.7, width=170, height=100, anchor='center')
lable5.place(relx=1, y=0, anchor='ne')

root.mainloop()


print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')
root = Tk()
setWindow(root)

lable = Label(root, text='Авторизация', font='Tahoma 20', width=10, height=2)
lableLogin = Label(root, text='Login', font='Tahoma 20', height=1)
lablePassword = Label(root, text='Password', font='Tahoma 20', height=1)
entry1 = Entry(root, font='Verdana 20', bg='#ddd', bd=1, width=7)
entry2 = Entry(root, font='Verdana 20', bg='#ddd', bd=1, width=7, show='*')
button1 = Button(root, text='Войти', font='Tahoma 20', bg='#bbb', fg='#fff', width=10)

lable.place(relx=.5, y=0, anchor='n')
lableLogin.place(relx=.5, rely=.1, anchor='ne')
lablePassword.place(relx=.5, rely=0.2, anchor='ne')
entry1.place(relx=.5, rely=.1, anchor='nw')
entry2.place(relx=.5, rely=.2, anchor='nw')
button1.place(relx=.5, rely=.35, anchor='center')

root.mainloop()