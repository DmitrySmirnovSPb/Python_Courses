from tkinter import *
from setWindow import *

root = Tk()
setWindow(root)

label1 = Label(root, text="Метка 1", font="Tahoma 20", bg="red")
label2 = Label(root, text="Метка 2", font="Tahoma 20", bg="green")
label3 = Label(root, text="Метка 3", font="Tahoma 20", bg="blue")
label4 = Label(root, text="Метка 4", font="Tahoma 20", bg="#9a3")
label5 = Label(root, text="Метка 5", font="Tahoma 20", bg="#777")

label1.grid(row=0, column=0, padx=10, pady=20)
label2.grid(row=0, column=1, ipadx=10, ipady=20)
label3.grid(row=1, column=0, columnspan=2, pady=20, ipadx=40)
label4.grid(row=2, column=0, rowspan=2, sticky="w")
label5.grid(row=2, column=1, sticky="nw")
Label(root, text="Метка 6", font="Tahoma 20", bg="#abf").grid(row=3, column=1, sticky="se")

root.mainloop()

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

root = Tk()
setWindow(root)

frame = Frame(root, bd=2)

lable = Label(frame, text='Авторизация', font='Tahoma 20', width=10, height=2)
lableLogin = Label(frame, text='Login', font='Tahoma 20', height=1)
lablePassword = Label(frame, text='Password', font='Tahoma 20', height=1)
entry1 = Entry(frame, font='Verdana 20', bg='#ddd', bd=1, width=7)
entry2 = Entry(frame, font='Verdana 20', bg='#ddd', bd=1, width=7, show='*')
button1 = Button(frame, text='Войти', font='Tahoma 20', bg='#bbb', fg='#fff', width=10)

frame.pack()
lable.grid(row=0, column=0, columnspan=2)
lableLogin.grid(row=1, column=0, sticky="w")
lablePassword.grid(row=2, column=0, sticky="w")
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button1.grid(row=3, column=0, columnspan=2)

root.mainloop()