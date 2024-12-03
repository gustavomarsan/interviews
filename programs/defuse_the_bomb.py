"""
https://leetcode.com/problems/defuse-the-bomb/
1652. Defuse the Bomb
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code 
of length of n and a key k.
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
Example 1:
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. 
Notice that the numbers wrap around.
Example 2:
Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 
Example 3:
Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
Constraints:
n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1
Note : Solve with sliding window [5,7,1,4]
                                  * * *         (window with the sum of k elements) (set the sum in the correct place)
                                  p1  p2
                       new_list  [0,0,0,0]

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
Moving slidewindow substrac p1 and add p2
"""

def defuse_bomb(code: list[int], k: int) -> list[int] :
	new_list = [0] *len(code)
	if k == 0 :
		return new_list
	p1 = 0
	p2 = abs(k) -1
	acum = 0
	for i in range(abs(k)) :
		acum += code[i]
	while p1 < len(code):
		if k > 0 :
			new_list[p1 -1] = acum
		else :
			new_list[(p2 + 1) % len(code)] = acum
		acum -= code[p1]
		p1 += 1
		p2 += 1
		p2 = p2 % len(code)
		acum += code[p2]
	return new_list

code = [5,7,1,4]
print(defuse_bomb(code, 3))
        
    
    

