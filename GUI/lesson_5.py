from tkinter import *
from setWindow import *
from codecs import *

root = Tk()
setWindow(root)

text = Text(root, font="Arial 12", bg="#ddd", fg='#555', width=25, height=5, pady=8, padx=10)
text.insert(END, 'Write')
print(text.get('1.0', END))

text.pack()
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

text = Text(root, font="Arial 12", bg="#ddd", fg='#555', width=50, height=5, pady=8, padx=10)
text.insert(END, txt)
print(text.get('1.0', END))

text.pack()
root.mainloop()
