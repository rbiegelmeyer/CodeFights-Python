def matrixElementsSum(matrix):
    s = 0;
    restrict = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                restrict.append(j)
            if (j not in restrict):
                s += matrix[i][j]
    return s