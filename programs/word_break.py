"""
139. Word Break
https://leetcode.com/problems/word-break/
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence 
of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
** Note: by using 2 pointers in the string check id the substring made by the 2 poniters is in the dict, if Yes 
delete word from dict, and the end, dict should be empty for True=
string = "catsandog"
          **
"""

def word_break(a: str, word_dict) :
    p1 = 0
    while p1 < len(a) :
        p2 = p1+1
        while p2 <= len(a) :
            if a[p1:p2] in word_dict :
                word_dict.discard(a[p1:p2])
                p1 = p2 -1
                break
            else :
                p2 +=1
        p1 += 1
    return len(word_dict) == 0


a1 = "catsandog"
word_dict1 = {"cats","dog","sand","and","cat" }
a2 = "applepenapple" 
word_dict2 = {"apple","pen"}
print(word_break(a1, word_dict1))
print(word_break(a2, word_dict2))
