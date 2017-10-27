def alternatingSums(a):
    teamA, teamB = [], []
    for i,x in enumerate(a):
        if (i%2 == 0):
            teamA.append(x)
        else:
            teamB.append(x)
    return sum(teamA),sum(teamB)

print (alternatingSums([50, 60, 60, 45, 70]))