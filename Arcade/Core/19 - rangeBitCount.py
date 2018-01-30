def rangeBitCount(a, b):
    retorno = 0
    for i in range(a,b+1):
        retorno += bin(i).count("1")
    return retorno