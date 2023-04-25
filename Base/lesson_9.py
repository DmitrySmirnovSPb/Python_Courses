list = []
print(list)
list = ['h','e','l','l','o']
print(list)

print(list[1])
print(len(list))
print(list[-1])
print("--------------------------------")

for i in list:
    print(i)

prices = [20,258,6,36,15,858,36]
min = prices[0]
max = prices[0]
i = 1
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max = prices[i]
    i += 1
print(max)
print(min)

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

array = ['one', 'two', 'tree', 'fore', 'five', 'six']
i = 0
for list in array:
    print(f'{i} - {list}')
    i += 1

while True:
    index = int(input('Введите индекс необходимого элемента'))
    if index == -1: break
    if index >= len(array) or index < 0: print(f'Вы ввели неверный индекс. Диапазон от 0 до {len(array) - 1}')
    else: print(array[index])
print(array[-len(array)])