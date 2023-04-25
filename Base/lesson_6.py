str1 = 'abc'
str2 = "xyz"
print("Конкатенация строк str1 и str2 = ", str1+str2)
str1 = '''Длинная строка
на несколько
строк'''

numder1 = input("Введите первое число: ")
print("Вы ввели число ", numder1)
numder2 = input("Введите второе число: ")
print("Вы ввели число ", numder2)
print("Введите третье число: ")
numder3 = input()
print("Вы ввели число ", numder3)
print("Сумма строк = ", numder1+numder2)
print("Сумма строк преобразованная в целое число = ", int(numder1+numder2))
print("Сумма чисел = ", int(numder1)+int(numder2))
print("Сумма чисел = ", float(numder1)+float(numder2))

print("Среднее арифметическое = ", (float(numder1)+float(numder2)+float(numder3))/3)