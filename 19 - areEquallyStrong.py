def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if (yourLeft == friendsLeft) and (yourRight == friendsRight):
        return True
    elif (yourRight == friendsLeft) and (yourLeft == friendsRight):
        return True
    else:
        return False


# def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
#     return True if ((yourLeft == friendsLeft) and (yourRight == friendsRight) or (yourRight == friendsLeft) and (yourLeft == friendsRight)) else False


#False
print (areEquallyStrong(10,5,7,10))
#rue
print (areEquallyStrong(10,5,5,10))
#rue
print (areEquallyStrong(10,5,10,5))
