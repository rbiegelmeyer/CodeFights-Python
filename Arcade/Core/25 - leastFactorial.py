def leastFactorial(n):
    cont = 1
    total = 1
    while total < n:
        cont += 1
        total = total * cont 
    return total