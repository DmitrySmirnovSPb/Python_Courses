import random

d = {'name':'Dmitry','age':52}
print(d)
d.setdefault('Sity', 'Saints-Petesburg')
d.setdefault('isWorking',True)
print(d)
d.pop('isWorking')
print(d)
print(list(d.keys()))

print(list(d.values()))

d['age'] = 40
d['mail'] = 'mail@mail.ru'

print(d)

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

dictionary = {
    'Hello' : 'Здравствуй',
    'Bye' : 'Пока',
    'Lesson' : 'Урок',
}

def inpStp(key):
    global dictionary
    text = f'Введите перевод на английский язык слова "{dictionary[key]}": '
    return input(text).lower()

keys = list(dictionary.keys())
flag = True
while True:
    if flag:
        tmp = random.randint(0, len(keys)-1)
    st = inpStp(keys[tmp])
    if st == 'quit':
        break
    elif st == 'show':
        for k in dictionary :
            print(f'"{dictionary[k]}" перевод на английский язык: {k}')
    else:
        if st == keys[tmp].lower():
            print('Ответ правильный! Молодец!')
            print()
            flag = True
        else:
            print('Попробуй еще раз.')
            flag = False