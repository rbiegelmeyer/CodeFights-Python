from itertools import combinations

def crazyball(players, k):
    return list(combinations(sorted(players), k))


players = ["Ninja",  "Warrior",  "Trainee",
           "Newbie"]
k = 3

print (crazyball(players,k))


# [["Newbie","Ninja","Trainee"], 
#  ["Newbie","Ninja","Warrior"], 
#  ["Newbie","Trainee","Warrior"], 
#  ["Ninja","Trainee","Warrior"]]