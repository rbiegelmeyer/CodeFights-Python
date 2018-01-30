def sumUpNumbers(inputString):
    soma = 0
    
    inputString = re.sub(r'[^0-9]', ' ', inputString)
    
    for x in inputString.split(" "):
        if x.isnumeric():
            soma += int(x)
    return soma