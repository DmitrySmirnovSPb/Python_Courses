handler = open('a.txt', 'w')
# модификатор w - открытие файла на запись с удалением содержимого, если файл отсутствуе, то создать
# модификатор x - открытие файла на запись с удалением содержимого, если файл отсутствует выбрасывается исключение
# модификатор a - открытие файла на запись с добавлением в конец файла
# модификатор rt - открытие файла на чтение в текстовом режиме //// по умолчанию
# модификатор rb - открытие файла на чтение в двоичном режиме

handler.write('abc 123\n895456')
handler.close()

handler = open('a.txt', 'rt')
print(handler.read(2))
print(handler.read())
handler.seek(0)
handler.seek(0)
print(handler.read())
handler.seek(0)
for line in handler:
    print(line)
handler.close()

link = 'b.txt'

while True:
    print('1 - Запись файла, 2 - Прочитать файл, 0 - Выход')
    inp = input('Введите команду: ')
    if inp == '0':
        break
    elif inp == '1':
        text = input('Введите строку для записи в файл: ')
        handler = open(link, 'w')
        handler.write(text)
        handler.close()
    elif inp == '2':
        try:
            hadler = open(link, 'rt')
            print(hadler.read())
            handler.close()
        except FileNotFoundError:
            print ('Файл не существует!')
    else:
        print('неизвестная команда.')
