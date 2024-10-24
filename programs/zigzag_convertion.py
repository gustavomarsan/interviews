"""
https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display 
this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

"""

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    lists = [[]for x in range(numRows)]
    way = 1
    arr = 0
    for item in s :
        lists[arr].append(item)
        if arr == numRows -1 :
            way = -1
        if arr == 0 :
            way = 1
        arr += way
    for i in range(numRows) :
        lists[i] = "".join(lists[i])
    return  "".join(lists)
        

        
s = "PAYPALISHIRING"
print(convert(s, 3))