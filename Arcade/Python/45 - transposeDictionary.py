def transposeDictionary(scriptByExtension):
    return sorted([[scriptByExtension[x],x] for x in scriptByExtension.keys()])


scriptByExtension = {
    "validate": "py",
    "getLimits": "md",
    "generateOutputs": "json"
}
print (transposeDictionary(scriptByExtension))

# [["json","generateOutputs"], 
#  ["md","getLimits"], 
#  ["py","validate"]]