"""
https://leetcode.com/problems/longest-common-prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(strs: list[str])-> str :
    prefix = strs[0]
    len_prefix = (len(prefix))
    for s in strs:
        while s[:len_prefix] != prefix:
            len_prefix -= 1
            prefix = prefix[:len_prefix]
            if len(prefix) == 0:
                return ""
    return prefix
            

    
    
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))