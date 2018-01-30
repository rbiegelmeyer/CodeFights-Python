def electionsWinners(votes, k):
    maior = max(votes)
    winners = 0
    for x in votes:
        if ((x+k)>maior):
            winners += 1
    if winners > 0:
        return winners
    else:
        if (votes.count(maior)==1):
            return 1
        return 0