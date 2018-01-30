def deleteDigit(n):
    lista = list(str(n))
    maior = 0
    
    for i in range(len(lista)):
        temp_list = lista[:i]+lista[i+1:]
        
        temp_num = int(''.join(map(str, temp_list)))
        
        if (temp_num > maior):
            maior = temp_num
    
    return maior