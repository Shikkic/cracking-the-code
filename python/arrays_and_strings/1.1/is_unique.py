
def is_unique(s):
    if len(s) < 1:
        return False

    characterDict = {}
    for char in s:
        if characterDict.has_key(char):
            return False
        else:
            characterDict[char] = 1

    return True
