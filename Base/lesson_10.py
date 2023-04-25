import random

array = [1, 0, 8, -5, 9]
for n in array:
    print(n)
print('------------------------------')
str ='Python'

for s in str:
    print(s)

for s in str:
    if s == "Y":
        break
else:
    print(f"Символа Y в строке {str} нет!")

print('------------------------------')
array = list(range(2,15))
for i in array:
    print(i)

ar = [i for i in range(1,20) if i % 2 == 0]
print(ar)

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

start = -1000
finish = 1000
count = random.randint(3, 18)
lst = [random.randint(start, finish) for i in range(count)]

print(lst)
summ = 0

for num in lst:
    summ += num
print(f'Сумма чисел из массива lst длиной {len(lst)} будет: {summ}. \n А среднее арифметическое составит {summ / len(lst)}')