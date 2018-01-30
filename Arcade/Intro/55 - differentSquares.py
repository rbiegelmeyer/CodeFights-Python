def differentSquares(matrix):
    lista = []
    retorno = 0
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            temp = [matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1],matrix[i][j]]
            if not temp in lista:
                lista.append(temp)
                retorno += 1
    return retorno