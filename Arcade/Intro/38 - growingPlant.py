def growingPlant(upSpeed, downSpeed, desiredHeight):
    atual = upSpeed
    cont = 1
    while (atual < desiredHeight):
        if atual > desiredHeight:
            return cont
        else:
            atual = atual - downSpeed + upSpeed
            cont += 1
    return cont


print (growingPlant(100, 10, 910))