def digitDegree(n):
    degree = 0
    while len(str(n)) > 1:
        n = sumOfDigits(str(n))
        degree += 1
    return degree

def sumOfDigits(k):
    s = 0
    for c in k:
        s += int(c)
    return s