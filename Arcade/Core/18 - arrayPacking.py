def arrayPacking(a):    
    ret = 0
    for i in range(len(a)):
        ret |= a[i]<<8*i
    return ret