def sortByHeight(a):
    	listAux = []
	for x in a:
		if x >= 0:
			listAux.append(x)
			listAux.sort()
	for i,x in enumerate(a):
		if x == -1:
			listAux.insert(i,x)
	print (listAux)
	return listAux