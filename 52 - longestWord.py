def longestWord(text):
    maior = ""
    tamanho = 0
    
    text = removeSymbols(text)
    for x in text.split(" "):
        if (len(x) > tamanho):
            maior = x
            tamanho = len(maior)
        
    return maior
    
def removeSymbols(text):
    for char in ",![]":
        text = text.replace(char, " ")
    return text