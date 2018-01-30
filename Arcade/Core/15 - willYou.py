def willYou(t1, t2, t3):
    if (not t1 or not t2) and t3:
        return True
    elif (t1 and t2 and not t3):
        return True
    else:
        return False