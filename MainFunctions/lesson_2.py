s1 = 'string_1'
print(len(s1))
print(s1[1])
print(s1[-1])
print(s1[-2])
print(s1[1:6])

s1 = 'abc\n->xyz'
s2 = r'abc\n->xyz'
print(s1)
print(s2)

s3 = 'Hello '
print (s3 * 3)

print(s2.find('-'))
print('5426'.isdigit())
print('Hello'.isalpha())
print(s2.upper())
print('SHHYGGFDR'.lower())

print(ord('A'))
print(chr(125))

sl = '     Fghdjkuw Ghbwueijhwo    '
print(sl)
print(sl.strip())

sl = 'Здравствуйте, {0}! Вы из города {1}? Верно?'
print(sl.format('Дмитрий', 'Санкт-Петербург'))

sl = 'Здравствуйте, {name}! Вы из города {city}? Верно?'
print(sl.format(name='Дмитрий', city='Санкт-Петербург'))

data  = ('Дмитрий', 'Санкт-Петербург')
sl = 'Здравствуйте, {0[0]}! Вы из города {0[1]}? Верно?'
print(sl.format(data))

s1 = 'int: {0:d}; bin: {0:b}'
print(s1.format(5))

s1 = 'Round (150 / 47): {0:0.3}'
print(s1.format(150 /47))

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

str = input('Введите произвольную строку: ')

for i in str:
    print(f'Символ {i} имеет код:',ord(i))

try:
    num = input('Пожалуйста введите только цифры')
    if(num.isdigit()):
        print('Спасибо')
    else:
        raise Exception('Некорректный ввод!')
except Exception as exp:
    print(exp)
