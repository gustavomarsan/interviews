"""
https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
Given an array of strings strs, group the angrams together. You can return the answer in any order.
Exemple 1 
input : ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
 
"""
from collections import defaultdict 

def groupAnagrams(strs):    #I made it. it breaks in longer lists
    my_dict = {}
    for item in strs :
        key = "".join(sorted(item))
        new_list = my_dict.get(key,[])
        new_list.append(item)
        my_dict[key] = new_list
    return [value for value in my_dict.values()]


def groupAnagrams2(strs)  :    #form leecode
    ans = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)
        
    return ans.values()
        
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams2(strs))
print(groupAnagrams(strs))


