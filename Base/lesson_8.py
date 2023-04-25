i = 0
while i < 10:
    i += 1
    print("hello World")
else: print("Цикл завершён")

print("------------------------------")
i = 0
while i < 10:
    print(i)
    i += 1
else: print("Цикл завершён")

print("------------------------------")
i = 0
while i < 10:
    i += 1
    if i == 5: continue
    elif i == 8: break
    print(i)
print("Цикл завершён, i =", i)

print("------------------------------")
s = 0
x = 1
to = 10
while x <= to:
    s += x
    x += 1
print(f"Сумма чисел от 1 до {to} равна {s}")
suma = 0
while True:
    codeInput = input("Введите число или комаду (Summ, exit или quit)")
    if codeInput == "exit" or codeInput == "quit":
        break
    elif codeInput == "summ":
        print("Сумма Введённых чисел = ", suma)
        suma = 0
    else:
        suma += float(codeInput)