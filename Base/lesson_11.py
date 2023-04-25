import random
myset = set('Python')
print(myset)
myset = {'1', 1, 2, 3, '1'}
print(myset)

lst = [random.randint(0, 10) for i in range(random.randint(5, 10))]
print(lst)
setlst = list(set(lst))
print(setlst)

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

ln = int(input('Введите длину списка '))
array = [random.randint(0, 100) for it in range(ln)]
i = 0
while i < len(array):
    print(array[i])
    i += 1
print('+-----------------------------------+')
array = list(set(array))
for val in array:
    print(val)