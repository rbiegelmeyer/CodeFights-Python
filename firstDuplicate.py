def firstDuplicate(a):
    temp = set()
    for x in a:
        if x in temp:
            return x
        else:
            temp.add(x)
    return -1


print (firstDuplicate([2, 3, 3, 1, 5, 2]))
print (firstDuplicate([2, 4, 3, 5, 1]))
