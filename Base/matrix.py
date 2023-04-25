matrix = [
    [3, 2, 6],
    [1, 3, 1],
    [4, 2, 1]
]

def matrixDeterminant(matrix):
    lineCount = len(matrix)
    for line in matrix:
        if len(line) != lineCount:
            raise Exception('Ошибка матрицы!\nПроверте количество строк и сталбов.')
    for i in range(lineCount):
        