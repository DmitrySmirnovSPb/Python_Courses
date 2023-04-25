from tkinter import *
from setWindow import *

root = Tk()
setWindow(root)

frame1 = Frame(root, bg='#00f', bd=2)
frame2 = Frame(root, bg='#0f0', bd=2)

lable1 = Label(frame1, text='Метка 1')
lable2 = Label(frame2, text='Метка 2')
lable3 = Label(frame2, text='Метка 3')

frame2.pack()
frame1.pack()
lable1.pack()
lable3.pack()
lable2.pack()

root.mainloop()


print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')
root = Tk()
setWindow(root)

frame1 = Frame(root)
frame2 = Frame(root, bg='#0f0', bd=2)
frame3 = Frame(root, bg='#f00', bd=2)

lable1 = Label(frame1, text='Важная форма')
entry1 = Entry(frame2, font='Verdana 20', bg='#ddd', fg='green', bd=1)
button1 = Button(frame3, text='Отправить форму', font='HondaC 18', bg='#bbb', fg='#fff')
button1.pack()

frame1.pack()
frame2.pack()
frame3.pack()
lable1.pack()
entry1.pack()

root.mainloop()