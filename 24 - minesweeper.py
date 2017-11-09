def increment(row, col, ret):
    row, col = row+1, col+1
    for l in range(row - 1, row + 2):
        for m in range(col - 1, col + 2):
            ret[l][m] += 1
    return ret

def minesweeper(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    retorno = [[0 for y in range(cols + 2)] for x in range(rows + 2)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]:
                increment(i, j, retorno)
                retorno[i+1][j+1] -= 1 #own trap decrement

    return [x[1:cols+1] for x in retorno[1:rows+1]]

print (minesweeper([[1, 0, 0], [0, 1, 0], [0, 0, 0]]))
print (minesweeper([[0, 0, 0], [0, 0, 0]]))
print (minesweeper([[1, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1]]))
