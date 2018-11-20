def pressureGauges(morning, evening):
    return [min(a,b) for a,b in zip(morning,evening)], [max(a,b) for a,b in zip(morning,evening)]


morning = [3, 5, 2, 6]
evening = [1, 6, 6, 6]

print (pressureGauges(morning,evening))


#[[1,5,2,6],[3,6,6,6]]