def areSimilar(a, b):
    differentPairs = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            differentPairs += 1
    if differentPairs < 2:
        return True
    if differentPairs == 2:
        if sorted(a) == sorted(b):
            return True
    return False



# def areSimilar(a, b):
#     if a == b:
#         return True
#     i = 0
#     while i<len(a):
#         if a[i] == b[i]:
#             a.pop(i)
#             b.pop(i)
#         else:
#             i += 1
#     if len(a)!=2:
#         return False
#     b[0], b[1] = b[1], b[0]
#     if a == b:
#         return True
#     else:
#         return False


# def areSimilar(a, b):
#     cont = 0
#     for x in a:
#         if a.count(x) != b.count(x):
#             return False
#     for i in range(len(a)):
#         print (i)
#         if a[i] != b[i]:
#             cont += 1
#             if cont>2:
#                 return False
#     return True


#True
print areSimilar([1, 2, 3], [1, 2, 3])    
#True
print areSimilar([1, 2, 3], [2, 1, 3])
#False
print areSimilar([1, 2, 2], [2, 1, 1])
#True
print areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 998, 148, 570, 533, 561, 455, 147, 894, 279])
#False
print areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279])
#True
print areSimilar([2, 1, 2, 1, 1, 1, 2], [1, 1, 2, 1, 2, 1, 2])
#True
print areSimilar([1, 2, 1, 2, 1, 2], [1, 1, 1, 2, 2, 2])
#True
print areSimilar([1, 2, 1, 2, 1, 2], [1, 1, 1, 2, 2, 2])
#False
print areSimilar([4, 6, 3], [3, 4, 6])
#False
print areSimilar([1, 2, 2, 2], [1, 1, 1, 2])