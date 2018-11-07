from string import maketrans
def permutationCipher(password, key):
    table = maketrans("abcdefghijklmnopqrstuwxyz", outtab)
    return password.translate(table)
