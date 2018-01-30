def boxBlur(image):
    row = len(image)
    col = len(image[0])

    retorno = [[] for x in range(row - 2)]

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            row1 = sum(image[i - 1][j - 1:j + 2])
            row2 = sum(image[i][j - 1:j + 2])
            row3 = sum(image[i + 1][j - 1:j + 2])

            retorno[i - 1].append((row1 + row2 + row3) // 9)

    return retorno


print (boxBlur([[1, 1, 1], [1, 7, 1], [1, 1, 1]]))
print (boxBlur([[0, 18, 9], [27, 9, 0], [81, 63, 45]]))
print (boxBlur([[36, 0, 18, 9], [27, 54, 9, 0], [81, 63, 72, 45]]))
print (boxBlur([[7, 4, 0, 1], [5, 6, 2, 2], [6, 10, 7, 8], [1, 4, 2, 0]]))
print (boxBlur([[36, 0, 18, 9, 9, 45, 27], [27, 0, 54, 9, 0, 63, 90], [81, 63, 72, 45, 18, 27, 0], [
       0, 0, 9, 81, 27, 18, 45], [45, 45, 27, 27, 90, 81, 72], [45, 18, 9, 0, 9, 18, 45], [27, 81, 36, 63, 63, 72, 81]]))
