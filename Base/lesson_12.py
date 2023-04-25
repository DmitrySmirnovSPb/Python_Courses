mytuple = (1, 2.5, '1', '1')
print(mytuple[1])
# создание кортежа с одним элементом
tl = (5,)
print(tl)

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

strInput = input('Введите произвольную строку: ')
strTuple = tuple(strInput)

for st in strTuple:
    print(st)
