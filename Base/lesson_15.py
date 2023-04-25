def dl(x,y):
    print(x / y)

def sum(x,y):
    s = f(x) + f(y)
    if isPrint:
        print(f'Сумма {s}')
    else:
        return s
def sub(x,y):
    global result
    result = f(x) - f(y)

f = lambda x : float(x)

dl(10, 2)
dl(y=10, x=2)

isPrint = False
result = 0
print('Result =',result)

x = input('Введите первое число: ')
y = input('Введите второе число: ')

print('Сумма равна: ', sum(x,y))
isPrint = True
sum(x,y)
sub(x,y)
print(result)


print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

PI = (3.141592,)

def PlOcr(r):
    return PI[0]*r**2

print(PlOcr(1))
print(PlOcr(10))
print(PlOcr(PI[0]))