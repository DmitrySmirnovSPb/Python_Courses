from tkinter import *
from setWindow import *

root = Tk()
setWindow(root)

text = Text(root, bd=2, font='Calibri 16', bg='#bbb', fg='Green', width=50)

scrollbar = Scrollbar(root, command=text.yview(), orient=VERTICAL)

text['yscrollcommand'] = scrollbar.set


text.pack(side='left')
scrollbar.pack(side='left', fill=Y)

root.mainloop()


print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

link = 'newText.txt'
mod = 'rt'
handler = open(link, mod)
txt = handler.read()
handler.close()
root = Tk()
setWindow(root)

text = Text(root, bd=2, font='Calibri 16', bg='#bbb', fg='#555', width=50)
text.insert(END, txt)
scr = Scrollbar(root, command=text.yview(), orient=VERTICAL)
text['yscrollcommand'] = scr.set
text.pack(side='left')
scr.pack(side='left', fill=Y)
root.mainloop()