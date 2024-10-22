"""
https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal 
place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, 
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, 
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms 
are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot 
append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.
Example 1:
Input: num = 3749
Output: "MMMDCCXLIX"
Explanation:
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:
Input: num = 58
Output: "LVIII"
Explanation:
50 = L
 8 = VIII
Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation:
1000 = M
 900 = CM
  90 = XC
   4 = IV
 
Constraints:

1 <= num <= 3999
"""


def intToRoman(num: int)-> str:
    roman = ""
    list_num = [int(x) for x in str(num)]
    if len(list_num) == 4 :					# thousends
        for i in range(list_num[0]) :
            roman += "M"
    if len(list_num) > 2 :					# hundresds
        if list_num[-3] == 9 :
            roman += "CM"
        elif list_num[-3] == 4 :
            roman += "CD"
        else :
            if list_num[-3] > 4 :
                list_num[-3] -= 5
                roman += "D"
            for i in range(list_num[-3]) :
                roman += "C"
    if len(list_num) > 1 :					# tens
        if list_num[-2] == 9 :
            roman += "XC"
        elif list_num[-2] == 4 :
            roman += "XL"
        else :
            if list_num[-2] > 4 :
                list_num[-2] -= 5
                roman += "L"
            for i in range(list_num[-2]) :
                roman += "X"
    if len(list_num) > 0 :					# units
        if list_num[-1] == 9 :
            roman += "IX"
        elif list_num[-1] == 4 :
            roman += "IV"
        else :
            if list_num[-1] > 4 :
                list_num[-1] -= 5
                roman += "V"
            for i in range(list_num[-1]) :
                roman += "I"
    return roman
                
num = 58
print(intToRoman(num))