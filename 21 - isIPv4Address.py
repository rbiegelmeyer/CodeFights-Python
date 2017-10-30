def isIPv4Address(inputString):
    list = inputString.split('.')
    if len(list) != 4:
        return False 
    for x in list:
        if len(x) == 0:
            return False
        elif not x.isnumeric():
            return False
        elif int(x) < 0 or int(x) > 255:
            return False
    return True

#True
print (isIPv4Address("172.16.254.1"))
#False
print (isIPv4Address("172.316.254.1"))
#False
print (isIPv4Address(".254.255.0"))
#False
print (isIPv4Address("1"))
#True
print (isIPv4Address("0.254.255.0"))
