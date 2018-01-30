def extractEachKth(inputArray, k):
    j = k
    while (j <= len(inputArray)):
        del inputArray[j-1]
        j += k-1

    return inputArray