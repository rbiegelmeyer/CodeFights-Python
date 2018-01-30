def fileNaming(names):
    retorno = []
    for x in names:
        cont = isRetorno(x, retorno)
        if cont == 0:
            retorno.append(x)
        else:
            retorno.append(x+"("+str(cont)+")")
    return retorno
        
def isRetorno(name, ret):
    cont = 0
    temp_name = name
    while temp_name in ret:
        cont += 1
        temp_name = name+"("+str(cont)+")"
    return cont