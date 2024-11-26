"""
https://leetcode.com/problems/add-binary/
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

def addBinary(a: str, b: str)-> str:
        result = [] 
        carry = 0
        i = len(a) -1
        j = len(b) -1
        while i >= 0 or j >= 0 or carry :
            partial = carry
            if i >= 0 :
                partial += int(a[i])
                i -= 1
            if j >= 0 :
                partial += int(b[j])
                j -= 1
            result.append(str(partial % 2))
            carry = partial // 2
        return "".join(result[::-1])
      
a = "1010"
b = "1011"
print(addBinary(a, b))
    		
