def checkPalindrome(inputString):
    if ((inputString.islower()) and (len(inputString)>0)):
        return inputString==inputString[::-1]