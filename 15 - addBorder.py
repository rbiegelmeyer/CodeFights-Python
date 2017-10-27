def addBorder(picture):
    matrix = []
    borderSupInf = ""

    for i in range(len(picture[0])+2):
        borderSupInf += "*"

    matrix.append(borderSupInf)
    for x in picture:
         matrix.append("*" + x + "*")
    matrix.append(borderSupInf)

    return matrix
        
print (addBorder(["a"]))