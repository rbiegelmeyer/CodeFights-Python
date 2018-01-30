def knapsackLight(v1, w1, v2, w2, maxW):
    if maxW >= w1 + w2:
        return v1 + v2
    elif maxW < w1 and maxW < w2:
        return 0
    elif v1 >= v2:
        if maxW >= w1:
            return v1
        else:
            return v2
    else:
        if maxW >= w2:
            return v2
        else:
            return v1