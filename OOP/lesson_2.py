class Point:
     x = 0
     y = 0

p1 = Point()
print(p1)
print(p1.x, ':', p1.y)

p1.x = 5
print(p1.x, ':', p1.y)

p2 = Point()
p2.z = 10

print(p2.x, ':', p2.y, ':', p2.z)

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

class rectangle:

     x = 0
     y = 0
     h = 1
     w = 1

newRect = rectangle()

newRect.x = 18
newRect.y = -3
newRect.h = 175
newRect.w = 257

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