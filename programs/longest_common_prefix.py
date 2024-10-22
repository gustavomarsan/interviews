"""
https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
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
    prefix = ""
    count = 1
    while count <= len(strs[0]) :
        new_pre = strs[0][ :count]
        for item in strs :
            if len(item) < count or item[ :count] != new_pre :
                return prefix
        prefix = new_pre
        count +=1
    return prefix

     

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))