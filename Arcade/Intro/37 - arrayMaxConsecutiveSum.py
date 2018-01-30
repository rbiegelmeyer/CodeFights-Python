def arrayMaxConsecutiveSum(inputArray, k):
    total = high = sum(inputArray[0:k])

    for i in range(len(inputArray)-k):
        total = total - inputArray[i] + inputArray[i+k]
        if total > high:
            high = total

    return high