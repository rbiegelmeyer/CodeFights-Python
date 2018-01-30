def lineEncoding(s):
    cont = 0
    ant = s[0]
    retorno = ''
    for x in s:
        if x == ant:
            cont += 1
        else:
            if cont>1:
                retorno += str(cont)
            retorno += ant
            cont = 1
            ant = x
    if cont>1:
        retorno += str(cont)
    return retorno + ant
