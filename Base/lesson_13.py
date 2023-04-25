myDict = dict(name="John", age=35, isMan=True)
myDict = {'name':"John", "age":35, "isMan":True}
print(myDict)

for key in myDict:
    print(key, '=', myDict[key])

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

keys = ('Name', 'Age')
dct = dict(Name='Без имени', Age=-1)

dct['Name'] = input('Введите Ваше имя ')
dct['Age'] = int(input('Введите Ваш возраст '))
for key in dct:
    print(key, '=', dct[key])