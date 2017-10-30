def arrayChange(inputArray):
    last = inputArray[0]
    diferenca = 0
    retorno = 0
    for i in range(len(inputArray[1:])):
        if last >= inputArray[i+1]:
            print (last, ">=", inputArray[i])
            diferenca += 1 + last - (inputArray[i+1])
            retorno += diferenca
        last = inputArray[i+1] + diferenca
        diferenca = 0
    
    return retorno

print (arrayChange([1, 1, 1]))
print (arrayChange([-1000, 0, -2, 0]))