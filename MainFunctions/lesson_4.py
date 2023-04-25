import random

def newSet(number):
    result = set()
    while len(result) <= number:
        tmp = random.randint(0, 50)
        result.add(tmp)
    return result

set1 = {1,2,3}
set2 = {1,2,3,4}

print(len(set1))
set1.add(10)
print(set1)

set1.remove(10)
print(set1)

set1.discard(8)

print('---------------------')

print(set1 == set2)
print(set1 <= set2)
print(set1 >= set2)

print('---------------------')

print(set1.union(set2))
print(set1.intersection((set2)))
print(set1.difference(set2))
print(set2.difference(set1))

print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

setNew1 = newSet(10)
setNew2 = newSet(10)
print(setNew1)
print(setNew2)

print(setNew1.union(setNew2))
print(setNew1.difference(setNew2))
print(setNew2.difference(setNew1))
print(setNew1.intersection(setNew2))