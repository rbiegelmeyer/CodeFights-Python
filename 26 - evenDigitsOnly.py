def evenDigitsOnly(n):
    listaux = [int(x) for x in str(n)]
    for x in listaux:
        if (x%2==1):
            return False
    return True

print (evenDigitsOnly(243))