def wordPower(word):
    num = dict(zip(list(word), [ord(x)-96 for x in word]))
    return sum([num[ch] for ch in word])
