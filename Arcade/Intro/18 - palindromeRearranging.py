def palindromeRearranging(inputString):
    characters = set(inputString)
    t = False   
    for x in characters:
        if ((inputString.count(x)%2 == 1) and (t == True)):
            return False
        elif ((inputString.count(x)%2 == 1) and (t == False)):
            t = True
    return True

#True
print (palindromeRearranging("aabb"))
# #False
print (palindromeRearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"))
# #True
print (palindromeRearranging("abbcabb"))
# #True
print (palindromeRearranging("zyyzzzzz"))
# #True
print (palindromeRearranging("z"))
# #True
print (palindromeRearranging("zaa"))
# #False
print (palindromeRearranging("abca"))
