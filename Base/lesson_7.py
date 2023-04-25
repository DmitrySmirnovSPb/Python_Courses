cont = True
while cont:
    print("Введите 0, 1 или 2: ")
    a = input()
    cont = not(a == "0" or a == "1" or a == "2")
    if a == "0":
        print("Выввели 0")
    elif a == "1":
        print("Выввели 1")
    elif a == "2":
        print("Вы ввели 2")
    else:
        print("Я же просил ввести 0, 1 или 2! Что не понятно?")
    x = 0 if not cont else 3
    print(x)
# Д/З

number1 = int(input("Введите делимое: "))
number2 = int(input("Введите делитель: "))
print()
if number2 == 0: result = "БЕСКОНЕЧНАЯ БЕСКОНЕЧНОСТЬ!!!"
else: result = f"{number1} / {number2} = " + str(number1 / number2)
print('''Результат деления:
+-----------------------------+
'''+result+"\n+-----------------------------+")