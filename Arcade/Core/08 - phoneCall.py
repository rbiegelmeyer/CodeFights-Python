def phoneCall(min1, min2_10, min11, s):
    retorno = 0
    if s - min1 >= 0:
        s = s - min1
        retorno = 1
    else:
        return retorno
    
    cont = 0
    while s >= min2_10 and cont < 9:
        s = s - min2_10
        cont += 1
        if s < min2_10 and cont < 9:
            return retorno + cont
    retorno += cont
        
    cont = 0 
    while s >= min11:
        s = s - min11
        cont += 1
        
    return retorno + cont