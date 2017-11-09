def alphabeticShift(inputString):
    str1 = ""
    for i, x in enumerate(inputString):
        str1 += chr(ord(x) + 1 if not ord(x) == 122 else 97)
    return str1


print (alphabeticShift("hhuuhzuhahuazhuahzhuahzhuazhahuzahzaabzzzzzzbz"))
print (ord("z"))