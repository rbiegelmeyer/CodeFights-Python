def magicalWell(a, b, n):
    result = 0
    for i in range(n):
        result += (a + i) * (b + i)
    return result