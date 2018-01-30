def sudoku(grid):
    for x in grid:
        for y in x:
            if x.count(y)>1:
                return False
                
    for i in range(9):
        rotate = []
        for j in range(9):
            rotate.append(grid[j][i])
        for x in rotate:
            if rotate.count(x)>1:
                # print (i)
                return False
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            lista = [grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]
            for x in lista:
                if lista.count(x) > 1:
                    return False
            
    return True