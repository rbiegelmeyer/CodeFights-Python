def reverseParentheses(s):
    for i in range(s.count('(')):
        fP, lP = s.rfind('(')+1, s.find(')',s.rfind('('))
        text = s[fP:lP]
        text = text[::-1]
        s = s[:fP-1] + text + s[lP+1:]
    return s

print (reverseParentheses("abc(cba)ab(bac)c"))