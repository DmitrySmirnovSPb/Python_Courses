def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return False
    return a/b

def sumArray(arList):
    result = 0
    for number in arList:
        result += number
    return result

def minArray (List):
    res = List[0]
    for l in List:
        if l < res:
            res = l
    return res

def maxArray(List):
    res = List[0]
    for l in List:
        if l > res:
            res = l
    return res
