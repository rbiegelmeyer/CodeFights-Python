def centuryFromYear(year):
    retorno = year/100
    if (year<=2005 and year>=1):
        if (int(retorno)<retorno):
            return (int(retorno)+1)
        else:
            return (int(retorno))