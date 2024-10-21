"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 
Example 1 : 
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

def wordPattern(pattern, s):
    p_p = 0
    p_w = 0
    my_dict = {}
    while p_p < len(pattern) :
        letter = pattern[p_p]
        p_p += 1
        word = ""
        while p_w < len(s) and s[p_w] != " " :
            word += s[p_w]
            p_w += 1
        if p_w == len(s) and p_p != len(pattern) :      # if words finish and pettern not
            return False
        while p_w < len(s) - 1 and s[p_w] == " " :
            p_w += 1
        if letter in my_dict and my_dict[letter] != word :
            return False
        elif letter not in my_dict and word in my_dict.values() :
            return False
        elif letter not in my_dict :
            my_dict[letter] = word
    print(p_p, len(pattern), p_w, len(s))
    return p_p ==len(pattern) and p_w == len(s)   # if patter finish and words not 

pattern = "he"
s = "unit"

print(wordPattern(pattern, s))