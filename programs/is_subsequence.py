"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "aaxc", t = "ahbgdc"
Output: false

in ordered way
"""

def isSubsequence(s, t):
    pointer = 0
    founds = 0
    for item in s :
        while pointer < len(t) :
            if item == t[pointer] :
                pointer +=1
                founds += 1
                break
            pointer += 1

    return founds == len(s)
        

s = "abc" 
t = "ahbgdc"
print(isSubsequence(s, t))