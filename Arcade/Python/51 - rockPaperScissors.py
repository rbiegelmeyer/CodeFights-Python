from itertools import permutations

def rockPaperScissors(players):
    return sorted(list(permutations(players,2)))


players = ["trainee",  "warrior",  "ninja"]
print (rockPaperScissors(players))

 #[["ninja","trainee"], 
#  ["ninja","warrior"], 
#  ["trainee","ninja"], 
#  ["trainee","warrior"], 
#  ["warrior","ninja"], 
#  ["warrior","trainee"]]