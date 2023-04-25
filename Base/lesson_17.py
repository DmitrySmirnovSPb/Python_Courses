try:
    a = float('abc')
except ValueError:
    print('Не возможно привести к числу')

while True:
    a = input('Введите положительное число: ')
    try:
        a = float(a)
        if a <= 0:
            raise Exception('Число отрицательное!')
    except ValueError:
        print('Не возможно привести к числу')
    except Exception as exp:
        print(exp)
    else:
        print('Спасибо за корректный ввод!')
    finally:
        print("В любом случае спасибо за попытку!")
    if a == 0:
        break

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

while True:
    try:
        a, b = input('Введите через пробел 2 числа, первое делимое, второй делитель: ').split()
    except ValueError:
        print('Вы не корректно ввели данные')
    else:
        if a == 'выход' or a == '0' or a == 'exit':
            break
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('Не возможно привести к числу')
        else:
            try:
                result = a / b
            except ZeroDivisionError:
                print('Делитель равен нулю, что не допустимо!\n\t\t\t\tПопробуйте ещё раз')
                continue
        print(result)