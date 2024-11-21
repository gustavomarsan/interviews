"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if 
needle is not part of haystack.
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
from datetime import datetime

def strStr(haystack: str, needle: str)-> int :
    #create a list of possible indexes
    my_list = [i for i in range(len(haystack)) if haystack[i] == needle[0] ]
    for item in my_list :       # just check in possible indexes
        if needle == haystack[item : item + len(needle)] :
            return item
    return -1

def strStr2(haystack, needle):
    for i in range((len(haystack) - len(needle)) + 1 ) :
        if needle == haystack[i : i + len(needle)] :
            return i
    return -1

a = "aaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaddsaaaaaaaaaaaaaaad"
b = "saaaaaaaaaaaaaaad"
ahora = datetime.now()
print(strStr(a,b))
print(datetime.now() - ahora)
ahora = datetime.now()
print(strStr2(a,b))
print(datetime.now() - ahora)
