"""
68. Text Justification
https://leetcode.com/problems/text-justification/
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters 
and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not 
divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.
Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:
Output:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

"""
from collections import deque
def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    def pack(paragraph: list[str], total_chars_words: int, empty : bool) -> str :
        if empty or len(paragraph) == 1 :
            new_string = " ".join(paragraph)
            while len(new_string) < maxWidth :
                new_string = new_string+" "
            result.append(new_string)    
            return
        words = len(paragraph)
        spaces = len(paragraph) -1
        free_chars = maxWidth - total_chars_words - spaces
        spaces_list = []
        for i in range(spaces) :
            spaces_list.append(" ")
        i = 0
        while free_chars > 0 :
            spaces_list[i%len(spaces_list)] = spaces_list[i%len(spaces_list)]+" "
            i +=1
            free_chars -= 1
        new_string = ""
        for i in range(len(paragraph) -1) :
            new_string += paragraph[i]
            new_string += spaces_list[i]
        new_string += paragraph[-1]
        result.append(new_string)
        return
    result = []
    de = deque(words)
    while len(de) > 0 :
        new_string = 0
        paragraph = []
        while len(de) > 0 and new_string < maxWidth :
            if len(paragraph) + new_string + len(de[0]) > maxWidth :
                break
            new_string += len(de[0]) 
            paragraph.append(de.popleft())
        pack(paragraph, new_string, len(de)== 0)
    return result




words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
max_width = 20
result =fullJustify(words, max_width)
for item in result :
    print(item)





