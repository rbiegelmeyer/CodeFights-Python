def addBorder(picture):
    matrix = []
    borderSupInf = (len(picture[0])+2)*"*"
    matrix.append(borderSupInf)

    for x in picture:
         matrix.append("*" + x + "*") 
    matrix.append(borderSupInf)
    
    return matrix