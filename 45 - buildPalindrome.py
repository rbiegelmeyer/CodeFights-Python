def buildPalindrome(st):
    s = len(st)
    for i in range(s):
        piece = st[i:s]
        if isPalindrome(piece):
            non = st[0:i]
            return st + non[::-1]

def isPalindrome(text):
    return text == text[::-1]