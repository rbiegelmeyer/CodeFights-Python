def firstNotRepeatingCharacter(s):
    temp = sorted(set(s), key=s.index)
    for x in temp:
        if not s.count(x) > 1:
            return x

    return "_"


print (firstNotRepeatingCharacter("abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"))