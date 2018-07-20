def variableName(name):
    if (name[0].isnumeric()):
        return False
    for x in name:
        if (not x.isalnum()) and (not x == "_"):
            return False
    return True