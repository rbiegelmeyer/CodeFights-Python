def chessBoardCellColor(cell1, cell2):
    clara = 0

    if ((ord(cell1[0]) % 2) == (int(cell1[1]) % 2)):
        clara = 1
    else:
        clara = 0

    if ((ord(cell2[0]) % 2) == (int(cell2[1]) % 2)):
        if (not clara):
            return False
    else:
        if (clara):
            return False

    return True


print (chessBoardCellColor("A1", "B2"))
