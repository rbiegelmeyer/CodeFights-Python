def arrayMaximalAdjacentDifference(inputArray):
    maior = 0
    for i in range(len(inputArray)-1):
        t = abs(inputArray[i] - inputArray[i+1])
        if maior < t: 
            maior = t
    return maior

print (arrayMaximalAdjacentDifference([2, 4, 1, 0]))
print (arrayMaximalAdjacentDifference([1, 1, 1, 1]))
print (arrayMaximalAdjacentDifference([-1, 4, 10, 3, -2]))
