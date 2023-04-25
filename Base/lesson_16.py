from random import *
import math as m

import calc as c

print(randint(1, 25))
print(int(m.sin(30*m.pi/180)*10+.000000001)/10)

while True:
    command = input('1 - умножение, 2- сложение, 3 - деление, 4 - вычитание ')
    if command == "exit" or command == '0' or command == 'quit':
        break
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    if command == '1':
        r = c.mult(a,b)
    elif command == '2':
        r = c.sum(a,b)
    elif command == '3':
        r = c.div(a,b)
    elif command == '4':
        r = c.sub(a,b)
    else:
        r = False
    if r != False:
        print(f'Результат вычисления {r}')
    else:
        print('Вы ввели ошибочный параметр')

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

print(c.maxArray([2,5,9,-12,2.9,11]))
print(c.minArray([2,5,9,-12,2.9,11]))
print(c.sumArray([2,5,9,-12,2.9,11]))