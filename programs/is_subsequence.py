"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "aaxc", t = "ahbgdc"
Output: false

in ordered way
"""
# O(nxm)  = O(n^2)
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
        
# O(n)
def isSubsequence_2(s, t):
    s_dict = {}
    t_dict = {}
    for item in s :
        s_dict[item] = s_dict.get(item, 0) + 1
    for item in t :
        t_dict[item] = s_dict.get(item, 0) + 1

    for key, value in s_dict.items() :
        if key not in t_dict or value > t_dict[key] :
            return False
    return True


#s = "abc" 
#t = "ahbgdc"
s = "aaxc"
t = "ahbgdc"
print(isSubsequence(s, t))
print(isSubsequence_2(s, t))