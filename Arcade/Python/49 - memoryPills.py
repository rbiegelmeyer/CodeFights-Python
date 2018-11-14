from itertools import dropwhile


def memoryPills(pills):
    gen = dropwhile(lambda x: len(x) & 1, pills + ['', '', ''])
    # print list(gen)
    next(gen)
    return [next(gen) for _ in range(3)]


pills = ["Med 1",
         "Med 2",
         "Med 3",
         "Med 10",
         "Med 11",
         "Med 12",
         "Med 14",
         "Med 42",
         "Med 239"]
print (memoryPills(pills))
# ["Med 11","Med 12","Med 14"]

pills = ["Notforgetan",  "Antimoron",
         "Rememberin",  "Bestmedicen",  "Superpillsus"]

print (memoryPills(pills))
# ["Bestmedicen", "Superpillsus", ""]
