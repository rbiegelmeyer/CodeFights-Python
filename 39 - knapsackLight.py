def knapsackLight(value1, weight1, value2, weight2, maxW):
    valor = 0
    if value1>value2:
        if weight1<=maxW:
            valor += value1
            maxW -= weight1
        if weight2<=maxW:
            return valor + value2
    else:
        if weight2<=maxW:
            valor += value2
            maxW -= weight2
        if weight1<=maxW:
            return valor + value1
    return valor

