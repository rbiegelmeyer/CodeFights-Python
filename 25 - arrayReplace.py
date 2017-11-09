def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i,x in enumerate(inputArray):
        if (x==elemToReplace):
            inputArray[i] = substitutionElem    

    return inputArray       


print (arrayReplace([1, 2, 1], 1, 3))
