from itertools import count, takewhile

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)


start = -0.9
stop = 0.45
step = 0.2


print (floatRange(start,stop,step))
# [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3]