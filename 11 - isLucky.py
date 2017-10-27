def isLucky(n):
    _str = str(n)
    firstHalf, lastHalf = _str[:len(_str)//2], _str[len(_str)//2:]
    return sum(map(int,firstHalf)) == sum(map(int, lastHalf))


    #fhalf = [int(i) for i in list(_str[:int(len(_str)/2)])]
	#lhalf = [int(i) for i in list(_str[int(len(_str)/2):])]
	#if sum(fhalf) == sum(lhalf):
	#	print ("T")
	#	return True
	#return False