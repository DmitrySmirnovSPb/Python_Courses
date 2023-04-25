from math import sqrt

class Point:

    x = 0
    y = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка с координатами ({self.x} : {self.y})'

    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y)**2)

class Auto:

    p = Point(0,0)
    speed = 0

    def __init__(self, p = Point(18,25), speed = 0):
        self.p = p
        self.speed = speed

    def setSpeed(self, speed):
        self.speed = speed

    def getTime(self, endP):
        if self.speed != 0:
            return self.p.range(endP) / self.speed
        else:
            return -1

p = Point(3,4)
print(p)

print(p.range(Point()))
print(p.range(Point(28,280)))

auto = Auto()
print(auto.speed)
print(auto.p.x)
auto.setSpeed(50)
print(auto.speed)

print(auto.getTime(Point(100, 200)))
print(auto.getTime(Point(18,25)))
auto.setSpeed(0)
print(auto.getTime(Point(100, 200)))

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

     def __str__(self):
         return f'Прямоугольник с координатами ({self.x}; {self.y}) шириной {self.w} и высотой {self.h}'

     def rectangleArea(self):
         return self.w * self.h

     def rectanglePerimeter(self):
         return 2*(self.h + self.w)

newRect = Rectangle(h = 6, w = 8)

print(newRect)
print('Периметр прямоугольника =',newRect.rectanglePerimeter())
print('Площадь прямоугольника =',newRect.rectangleArea())