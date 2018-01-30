def validTime(time):
    lista = time.split(":")
    if int(lista[0])>23 or int(lista[1])>59:
        return False
    return True