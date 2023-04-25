def printPython():
    print('Python')

def sum(x, y):
    return x+y

def sub(x,y):
    return x-y

def summaprint(x,y, r = False):
    s = sum(x,y)
    if r:
        return s
    else:
        print(s)
def printDict(**dict):
    for key in dict:
        print(key,'=>',dict[key])

printPython()

s = sum(7, 5)
print(s)
summaprint(7,23)

printDict(name='Dmitry',city='St. Petersburg',age=52)

lambdaFunc = lambda x,y: print(x+y)

lambdaFunc(13, 17)

print((lambda z,v: v ** z)(2,3))

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

def Chet(number):
    return number % 2 == 0

print(Chet(2))
print(Chet(5))

def maxList(ar):
    maxAr = ar[0]
    for i in ar:
        if i > maxAr: maxAr = i
    return maxAr

print(maxList([18, 25, 0, -85, 4, 15, 6, 78, 15, 52, 36, 25, -8531]))

def srAr(*ar):
    summa = 0
    for i in ar:
        summa += i
    return summa / len(ar)

print(srAr(1,5,8,6,5,8,46,8,6,-8))
print(srAr(1,2,3,4,5))