from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x: x[1].rotate(-x[0]),enumerate(res)), 0)
    return [list(d) for d in res]


digits = [1, 2, 3, 4, 5]

print (doodledPassword(digits))