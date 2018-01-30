def chessKnight(cell):
    x,y = ord(cell[0]),ord(cell[1])
    cont = 0
    if isValid(x+1,y+2):
        cont += 1
    if isValid(x+2,y+1):
        cont += 1
    if isValid(x-1,y+2):
        cont += 1
    if isValid(x-2,y+1):
        cont += 1
    if isValid(x-1,y-2):
        cont += 1
    if isValid(x-2,y-1):
        cont += 1
    if isValid(x+1,y-2):
        cont += 1
    if isValid(x+2,y-1):
        cont += 1
    return cont
    
def isValid(x,y):
    print (x, y)
    return ((x>=97) and (x<=104) and (y>=49) and (y<=56))