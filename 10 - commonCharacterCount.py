def commonCharacterCount(s1, s2):
    cont = 0
    for x in s1:
        if x in s2:
            s2 = s2.replace(x,"",1)
            cont += 1
    return cont