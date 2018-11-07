def getPoints(answers, p):
    questionPoints = lambda i,x: (i+1) if x else -p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res
