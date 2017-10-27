def areSimilar(a, b):
    retorno = True
    cont = 0
    for i,x in enumerate(a):
        if x != b[i]:
            cont += 1
            if cont>2:
                return False
            

    return retorno
    
#True
print areSimilar([1, 2, 3], [2, 1, 3])
#False
print areSimilar([1, 2, 2], [2, 1, 1])
#True
print areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 998, 148, 570, 533, 561, 455, 147, 894, 279])
#False
print areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279])