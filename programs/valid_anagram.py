"""
https://leetcode.com/problems/valid-anagram/submissions/1425901452/?envType=study-plan-v2&envId=top-interview-150
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original 
letters exactly once.
Example 1
Input: s = "anagram", t = "nagaram"
                  - 
Example 2
Input: s = "rat", t = "car"
Output: false

"""

def isAnagram(s, t):
    my_dict = {}
    for item in s :
        my_dict[item] = my_dict.get(item, 0) + 1
    for key, value in my_dict.items() : 
        if t.count(key) != value :
            return False
    return True
    
print(isAnagram(input("palabra 1: "),input("palabra 2: ")))