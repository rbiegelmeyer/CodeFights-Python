def adjacentElementsProduct(inputArray):
    high = inputArray[0]*inputArray[1]
    for x in range(len(inputArray)-1):
        temp = inputArray[x]*inputArray[x+1]
        if (temp>high):
            high = temp
    return high