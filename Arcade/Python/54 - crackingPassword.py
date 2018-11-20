from itertools import product


def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return list(filter(lambda x: int(x) % d == 0, map(createNumber, sorted(product(digits, repeat=k)))))


digits = [1, 5, 2]
k = 2
d = 3

print (crackingPassword(digits, k, d))

# ["12", "15",  "21",  "51"]
