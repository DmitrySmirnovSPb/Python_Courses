class Point:
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __test(self, str = ''):
        print(f'{str}Приватный метод')

    def runPrivate(self):
        self.__test('Запуск приватного метода с помощью public method runPrivate()\n')

p = Point(10, 15)

print('X до изменения',p.getX())
print('Y до изменения',p.getY())
p.setX(20)
p.setY(51)
print('X после изменения',p.getX())
print('Y после изменения',p.getY())

# print(p.__test()) # Выдает ошибку

p.runPrivate()

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

class Rectangle:

     __x = 0
     __y = 0
     __h = 1
     __w = 1

     def __init__(self, x = 0, y = 0, h = 1, w = 1):
         self.__x = x
         self.__y = y
         self.__h = h
         self.__w = w

     def __str__(self):
         return f'Прямоугольник с координатами ({self.__x}; {self.__y}) шириной {self.__w} и высотой {self.__h}'

     def rectangleArea(self):
         return self.__w * self.__h

     def rectanglePerimeter(self):
         return 2*(self.__h + self.__w)

     def getX(self):
         self.__printLog('координаита x', 'get')
         return self.__x

     def getY(self):
         self.__printLog('координаита y', 'get')
         return self.__y

     def getW(self):
         self.__printLog('Ширина', 'get')
         return self.__w

     def getH(self):
         self.__printLog('Высота', 'get')
         return self.__h

     def setX(self, x):
         self.__printLog('координаита x')
         self.__x = x

     def setY(self, y):
         self.__printLog('координаита y')
         self.__y = y

     def setW(self, w):
         self.__printLog('Ширина')
         self.__w = w

     def setH(self, h):
         self.__printLog('Высота')
         self.__h = h

     def __printLog(self, name, method='set'):
        if(method == 'get'):
            text = f'Запрошено свойство {name}'
        else:
            text = f'Изменено свойство {name}'
        print(text)

newRect = Rectangle(h = 6, w = 8)

print(newRect.getX())
print(newRect.getY())
print(newRect.getH())
print(newRect.getW())
print('Периметр прямоугольника =',newRect.rectanglePerimeter())
print('Площадь прямоугольника =',newRect.rectangleArea())

newRect.setY(86)
newRect.setX(68)
newRect.setW(5)
newRect.setH(4)

print(newRect.getX())
print(newRect.getY())
print(newRect.getH())
print(newRect.getW())
print('Периметр прямоугольника =',newRect.rectanglePerimeter())
print('Площадь прямоугольника =',newRect.rectangleArea())
