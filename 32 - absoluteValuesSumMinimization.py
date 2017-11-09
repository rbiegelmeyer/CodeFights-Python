def absoluteValuesSumMinimization(a):
    ret = 0
    aux = sum([abs(x) for x in a])
    for x in a:
        teste = 0
        for y in a:
            teste += abs(y - x)
        if (aux>teste):
            ret = x
            aux = teste

    return ret