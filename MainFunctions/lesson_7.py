from datetime import *
from time import *

print(date.today())
print(datetime.today())
d = date(2025,7,15)
print(d)

dt = datetime(2025, 7, 15, 15, 50, 30)
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print('-----------------')

print(dt.strftime('%Y.%m.%d %H:%M:%S'))
print(dt.strftime('%Y/%m/%d %H:%M:%S'))

print('-----------------')

print(time())

dt = datetime.fromtimestamp(1397859799)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print(dt.timestamp())

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

dateBD = []
bd = ('год', 'месяц', 'день')
for i in bd:
    text = f'Ввдите {i} вашего рождения: '
    dateBD.append(int(input(text)))
dt = datetime(dateBD[0], dateBD[1], dateBD[2])
dif= int(time()) - int(dt.timestamp())
print(f'С момента вашего рождения прошло {dif} секунд')
