"""""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

return "YES" or "NO"



"""

def twoStrings(s1, s2):
    # Write your code here
    my_dict = {}
    for i in range(0, len(s1)):
        for j in range(i+1, len(s1)+1):
            if s1[i:j] != s1 and s1[i:j] not in my_dict:
                my_dict[s1[i:j]] = 1
    for i in range(0, len(s2)):
        for j in range(i+1, len(s2)+1):
            if s2[i:j] in my_dict:
                return "YES"
    return "NO"

s1 = "be"
s2 = "cat"

print(twoStrings(s1, s2))