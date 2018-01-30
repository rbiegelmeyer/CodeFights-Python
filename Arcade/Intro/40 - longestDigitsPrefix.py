def longestDigitsPrefix(inputString):
    retorno = ""
    for i in range(len(inputString)):
        if inputString[i].isnumeric() or inputString[i] == '0':
            retorno += inputString[i]
        else:
            break   
    return retorno
    

print (longestDigitsPrefix("123aa1"))