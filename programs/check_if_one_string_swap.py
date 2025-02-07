"""
1790. Check if One String Swap Can Make Strings Equal
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string 
(not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. 
Otherwise, return false.
Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""

def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2 :
        return True

    s1_dict = {}    # dicts for values appearences
    s2_dict = {}
    for i in range(len(s1)) : # Fill dicts
        s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
        s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1
        
    if s1_dict != s2_dict :
        return False
        
    diff = 0        # we can allow only 2 differences to be one swap
    for i in range(len(s1)) :
        if s1[i] != s2[i] :
            diff += 1
        if diff > 2 :
            return False
    return True

#solution 2. I watched on let code is smart. Dont use a dict and is O(n) time complexity. O(1) Space
def areAlmostEqual_2(s1: str, s2: str) -> bool:
    if s1 == s2 :
        return True
    
    s1_diff = ["", ""]      # create a list for a allowed 2 diffs in s1
    s2_diff = ["", ""]      # create a list for a allowed 2 diffs in s2
    error = 0
    for i in range(len(s1)) :
        if s1[i] != s2[i] :
            if error  == 2 :
                return False
            s1_diff[error] = s1[i]      #set diff 1 and 2
            s2_diff[error] = s2[i]      #set diff 1 and 2
            error += 1
    
    if error == 1 :         # only one difference is false
        return False
    
    # return true if differences are inversed
    return s1_diff[0] == s2_diff[1] and s1_diff[1] == s2_diff[0]

s1 = "bank"
s2 = "kanb"
print(areAlmostEqual(s1, s2))
print(areAlmostEqual_2(s1, s2))