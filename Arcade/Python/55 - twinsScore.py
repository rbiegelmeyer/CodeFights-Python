def twinsScore(b, m):
    return (map(sum,zip(b,m)))

b = [22, 13, 45, 32]
m = [28, 41, 13, 32]

print (twinsScore(b,m))

# [50, 54, 58, 64]