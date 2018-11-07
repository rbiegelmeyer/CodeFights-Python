def allLongestStrings(inputArray):
    size = max(len(s) for s in inputArray)
    return [x for x in inputArray if len(x) == size]

print allLongestStrings(["aaa","dsds","dsfs"])