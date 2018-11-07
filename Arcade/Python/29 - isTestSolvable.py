def isTestSolvable(ids, k):
    digitSum = lambda x: sum(int(y) for y in str(x))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
