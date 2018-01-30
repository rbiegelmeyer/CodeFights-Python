import itertools


def stringsRearrangement(inputArray):

    def diff(x, y):
        aux = 0
        for i in range(len(x)):
            if (x[i] != y[i]):
                aux += 1
        if (aux == 1):
            return True
        return False

    for k in itertools.permutations(inputArray, len(inputArray)):
        r = True
        for i in range(len(k) - 1):
            if (not diff(k[i], k[i + 1])):
                r = False
        if r:
            return True

    return False


print (stringsRearrangement(["ab", "bb", "aa"]))
print (stringsRearrangement(["aba", "bbb", "bab"]))
