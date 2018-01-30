def bishopAndPawn(bishop, pawn):
    t1 = abs(ord(bishop[0])-ord(pawn[0]))
    t2 = abs(int(bishop[1])-int(pawn[1]))
    if (t1 == t2):
        return True
    return False