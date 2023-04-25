list = [1,2,0,5]
list[0] = 0
print(list)
list.append(9)
print(list)
list.extend([18,853,25,0])
print(list)
list.insert(1,777)
print(list)

print('---------------')

print(list.index(0))
print(list.index(0, 4))
print(list.count('a'))
print(list.count(0))

print('---------------')
list.reverse()
print(list)

list.remove(777)
print(list)
print(list.pop(6))
print(list)

list.sort(reverse=True)
print(list)

print('---------------')

t = tuple('Hello')
print(t.count('l'))
print(t.index('e'))

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

try:
    count = int(input('Введите количество элементов списка: '))
    list = []
    i = 0
    while i < count:
        try:
            newNumber = float(input(f'Введите число {i}: '))
            list.append(newNumber)
            i += 1
        except ValueError:
            print('Вы ввели не число')
    list.sort()
    print(list)
except ValueError:
    print('Не возможно привести к числу')