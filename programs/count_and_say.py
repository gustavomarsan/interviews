"""
https://leetcode.com/problems/count-and-say/
38. Count and Say
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) 
with the concatenation of the character and the number marking the count of the characters (length of the run). 
For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". 
Thus the compressed string becomes "23321511".
Given a positive integer n, return the nth element of the count-and-say sequence.

Example 1:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:
Input: n = 1
Output: "1"
Explanation:
This is the base case.
Constraints:
1 <= n <= 30
Follow up: Could you solve it iteratively?


"""
from time_counter import time_counter


class Solution:
    my_dict = {1 : "1"}

    def get_next_rle(self, prev: str)-> str:
        # calculate the next rle from the previous rle given by n
        new_rle = ""
        count = 1
        char = prev[0]
        for j in range(1, len(prev)):
            if prev[j] != char:
                new_rle = new_rle + str(count) + char
                char = prev[j]
                count = 1
            else:
                count += 1

        if count > 0:
            new_rle = new_rle + str(count) + char

        return new_rle
    
    def countAndSay(self, n: int) -> str:
        # return the rle of the previous rle given by n, if n is not in the dictionary, calculate it and save it in the dictionary
        if n in self.my_dict:
            return self.my_dict[n]
        
        else: 
            #calculate the desired rle and save it in the dictionary
            self.my_dict[n] = self.get_next_rle(self.countAndSay(n -1))

        return self.my_dict[n]
    
    @time_counter
    def print_rle(self, n: int):
        # print the rle for a number n
        print(n,"---->", self.countAndSay(n))
    
a = Solution()

a.print_rle(1)
a.print_rle(14)
a.print_rle(13)