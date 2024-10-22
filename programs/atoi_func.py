""""
https://leetcode.com/problems/string-to-integer-atoi/description/

Implement the myAtoi(string s) function, which converts a string to a signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. 
If no digits were read, then the result is 0.
 
Return the integer as the final result.

atoi("123") -> 123

" +123"   -> 123

"""

def my_atoi(s: str)-> int :
    v  = 1
    r = 0
    for n in range(len(s)) :
        if s[n] == " " :
            if r == 0 :
                continue
            else :
                break
        if (ord(s[n]) == 48 or s[n] == "+" or s[n] == "-") and r == 0 :
            if n == len(s) -1 or ord(s[n+1]) < 48 or ord(s[n+1]) > 57 :
                break
            elif s[n] == "-" :
                v *= -1
            continue
        if (ord(s[n]) < 48 or ord(s[n]) > 57 ) : 
            if r > 0 :
                break
            else :
                return 0
        
        else: 
            r = r*10 + int(s[n])
    
    if r*v < -2**31 :
        return  -2**31
    elif r*v > 2**31 -1 :
        return 2**31 -1
    else :
        return r*v
        
print(my_atoi("      -11919730356x"))
