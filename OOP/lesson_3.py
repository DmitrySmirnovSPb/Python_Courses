class Circle:

     x = 0
     y = 0
     r = 0

     def __init__(self, x, y, r = 0):
         self.x = x
         self.y = y
         self.r = r
         if r == 0:
             print('Радиус не задан')


c = Circle(5,7,10)
print(c.x,':',c.y,':',c.r)
c.x = 10
print(c.x)

c = Circle(5,20)
print(c.x,':',c.y,':',c.r)

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

class Rectangle:

     x = 0
     y = 0
     h = 1
     w = 1

     def __init__(self, x = 0, y = 0, h = 1, w = 1):
         self.x = x
         self.y = y
         self.h = h
         self.w = w

newRect = Rectangle(h = 58, w = 17, y = 2)

rec = {
     'x':'Координата X верхнего левого угла прямоугольника',
     'y':'Координата Y верхнего левого угла прямоугольника',
     'h':'Высота прямоугольника',
     'w':'Ширина прямоугольника'
}
for i in rec:
     if i == 'x':
          temp = newRect.x
     elif i == 'y':
          temp = newRect.y
     elif i == 'h':
          temp = newRect.h
     else:
          temp = newRect.w
     print(rec[i],':',temp)