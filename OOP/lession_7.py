from abc import ABC, abstractmethod

class Shape(ABC):

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        print(f'({self.x}) : {self.y}')

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):

    r = 0

    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r

    def draw(self):
        print(f'Рисуем окрудность с центром в ({self.x}:{self.y}), с радиусом {self.r}')

class Rectangle(Shape):

    w = 0
    h = 0

    def __init__(self, x, y, h, w):
        Shape.__init__(self, x, y)
        self.h = h
        self.w = w

    def draw(self):
        print(f'Рисуем прямоугольник с верхнис левым углом в ({self.x}:{self.y}), высотой {self.h}, шириной {self.w}')

Circle(151, 12, 8).draw()

Rectangle(15,25, 52, 58).draw()

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

class Motor:

    __fuel = 'A95'
    __power = 150
    __transmission = 'Automat'

class Auto(ABC):

    __type = 'auto'     # Тип автомобиля грузовик, легковой, кроссовер и так далее
    __speed = 0         # Текущая скорость автомобиля
    __x = 0             # Текущая кордината X
    __y = 0             # Текущая кордината Y
    __color = 'blue'    # Цвет автомобиля
    __number = ''       # Гос номер автомобиля
    __motor = Motor()   # Класс двигатель автомобиля

    def __init__(self, x=0, y=0, speed=0):
        self.__speed = speed
        self.__y = y
        self.__x = x

    @abstractmethod
    def moving(self, x, y):
        pass

class ix35(Auto):

    __passengers = 5
    condition = 'new'
    __equipment = 'lux'
    __model = 'Hyundai ix35'

    def __init__(self, number, color):
        Auto.__init__(self)
        self.__number = number
        self.__collor = color
        self.__motor = Motor
        self.__type = "Кроссовер"

    def moving(self, x, y):
        print(f'Движение {self.__model} в точку {x}, {y}')
        self.__x = x
        self.__y = y

class Lada(Auto):

    def moving(self, x, y):
        print(f'Движение Lada в точку {x}, {y}')
        self.__x = x
        self.__y = y


main = ix35(number='о828тв198', color='Серебристый')
main.moving(15,85)
Lada().moving(45,8)