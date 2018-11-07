def wordPower(word):
    num = dict(zip(list(word), [ord(x)-96 for x in word]))
    print (num)

    return sum([num[ch] for ch in word])

a = [4, 5, 6, 7, 8]
b = [8, 9, 10, 11, 12]

def coolPairs(a, b):
    uniqueSums = {x+y for x in a for y in b if (x*y)%(x+y) == 0}
    print (uniqueSums)
    return len(uniqueSums)

def multiplicationTable(n):
    return [[(x+1)*(y+1) for x in range(n)] for y in range(n)]

smarties = ["Jane", "Bob", "Peter"]
cleveries = ["Oscar", "Lidia", "Ann"]

def chessTeams(smarties, cleveries):
    return list(zip(smarties,cleveries))

ch = '*'
assignments = [12, 12, 14, 3, 12, 15, 14]
def createHistogram(ch, assignments):
    return [x*'*' for x in assignments]



# print coolPairs(a,b)

# print multiplicationTable(3)

# print chessTeams(smarties,cleveries)

print (createHistogram(ch,assignments))