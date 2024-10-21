"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false
s an l has the same lenght
"""


def isIsomorphic(s, t):
    my_dict = {} 
    for i in range(len(s)) :                                    #read string s and add to my_dict and comparing problems to exit
        if t[i] in my_dict.values() and s[i] not in my_dict :   #if value is in other key
            return False
        if s[i] in my_dict and my_dict[s[i]] != t[i] :          #if key has different value
            return False
        if s[i] not in my_dict :                                #if s[i] is a new k add to my_dict
            my_dict[s[i]] = t[i]
    return True 

print(isIsomorphic(input("palabra 1: "),input("palabra 2: ")))