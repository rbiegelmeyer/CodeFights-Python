def constructShell(n):
    return [[0] * (i+1) for i in range(n)] + [[0] * (n-i-1) for i in range(n-1)]
