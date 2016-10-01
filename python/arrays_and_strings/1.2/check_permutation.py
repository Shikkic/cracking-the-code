
# Given two strings, write a method to decide if one is a permutation of the other.
def check_permutation(s1, s2):
    if len(s1) is not len(s2):
        return False

    s1CharsDict = {}
    for char in s1:
        if s1CharsDict.get(char):
            s1CharsDict[char] += s1CharsDict.get(char, 1) +  1
    
    s2CharsDict = {}
    for char in s2:
        if s2CharsDict.get(char):
            s2CharsDict[char] += s2CharsDict.get(char, 1) +  1
    

    if s1CharsDict is not s2CharsDict:
        False

    return True

