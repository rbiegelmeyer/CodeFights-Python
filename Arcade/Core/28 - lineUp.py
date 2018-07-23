def lineUp(commands):
    cont = 0
    turned = False
    for x in commands:
        if (x == 'L' or x == 'R'):
            if turned:
                cont += 1
                turned = False
            else:
                turned = True
        if (x == 'A') and not turned:
            cont += 1
    return cont