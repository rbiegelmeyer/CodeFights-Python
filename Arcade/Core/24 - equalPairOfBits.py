def equalPairOfBits(n, m):
    return 2**(str(bin(~n ^ m)[::-1]).find('1'))