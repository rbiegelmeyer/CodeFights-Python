def messageFromBinaryCode(code):
    text = ""
    for i in range(int(len(code)/8)):
        text += chr(int(code[0+(i*8):8+(i*8)],2))
    return text