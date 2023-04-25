from datetime import *

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

def fileProgramm(command):
    if command == 'write':
        mod = 'a'
    else:
        mod = 'rt'
    try:
        handler = open(link, mod)
        if command == 'write':
            dt = datetime.today().strftime('%Y.%m.%d %H:%M:%S')
            title = f'\nПост от: {dt}\n'
            handler.write(f'{title}{text}\n')
        else:
            txt = handler.read()
            if command == 'copy':
                han = open(linkCopy, 'w')
                han.write(txt)
                han.close()
            else:
                print(txt)
        handler.close()
    except FileNotFoundError:
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!\nфайл по адресу:', link, 'не существует! Создайте файл или проверте правильность адреса.\n')

while True:
    print('"write" - Запись файла,\n"read" - Прочитать файл,\n"copy" - скопировать файл\n0 - Выход')
    inp = input('Введите команду: ')
    if inp == "write":
        message = "Напишите путь к файлу, который Вы хотите записать: "
        text = input('Введите текст, который вы хотите дополнить в файл: ')
    elif inp == 'copy':
        message = "Напишите путь к файлу, который Вы хотите скопировать: "
        linkCopy = input('Напишите адрес куда хотите скопировать файл: ')
    elif inp == 'read':
        message = 'Напишите путь к файлу, содержимое которого Вы хотите посмотреть: '
    elif inp == 'exit' or inp == 'quit' or inp == '0':
        break
    else:
        print('Команда не ясна! Повторите, пожалуйста!')
        continue
    link = input(message)

    fileProgramm(inp)