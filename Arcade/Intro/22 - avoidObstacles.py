def avoidObstacles(inputArray):
    s = len(inputArray) + max(inputArray)
    for step in range(2, s):
        k = -step
        for i in range(s):
            if k + step in inputArray:
                break
            k += step
        else:
            return step


print (avoidObstacles([5, 3, 6, 7, 9]))
print (avoidObstacles([2, 3]))
print (avoidObstacles([1, 4, 10, 6, 2]))