def tennisSet(score1, score2):
    if score1 > score2:
        if (score1 == 6 and score2 < 5) or (score1 == 7 and score2 >= 5):
            return True
        else:
            return False
    elif score2 > score1:
        if (score2 == 6 and score1 < 5) or (score2 == 7 and score1 >= 5):
            return True
        else:
            return False
    else:
        return False