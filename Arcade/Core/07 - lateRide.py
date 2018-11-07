def lateRide(n):
    h = str(int(n/60))
    if len(h)<2:
        h = "0"+h
        
    m = str(n%60)
    if len(m)<2:
        m = "0"+m
        
    return int(h[1])+int(h[0])+int(m[1])+int(m[0])