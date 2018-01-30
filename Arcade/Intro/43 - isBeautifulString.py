def isBeautifulString(inputString):
    maior = inputString.count('a')
    
    for i in range(98,123):
        print (inputString.count(chr(i)))
        if (inputString.count(chr(i)) > maior):
            return False
        else:
            maior = (inputString.count(chr(i)))
                     
    return True