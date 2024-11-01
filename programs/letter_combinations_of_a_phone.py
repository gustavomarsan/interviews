"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:
Input: digits = ""
Output: []
Example 3:
Input: digits = "2"
Output: ["a","b","c"]
Note: Backtracking solution
phone_keyboard =
		   0    1     2        3        4        5        6         7         8          9
letters = [[], [], [a,b,c], [d,e,f], [g,h,i], [j,k,l], [m,n,o], [p,q,r,s], [t,u,v], [w,x,y,z]]

 2<= numbers <= 9

"""
def backtracking(digits: str, results: list[str], partial: list[str], index: int) -> list[str]:
    letters = [[], [], ["a","b","c"], ["d","e","f"], ["g","h","i"], ["j","k","l"], ["m","n","o"], ["p","q","r","s"], ["t","u","v"], ["w","x","y","z"]]
	#stop backtracking
    if len(partial)  == len(digits) :
        if partial :
            results.append("".join(partial))
        return results
    element = int(digits[index])
    for i in range(len(letters[element])) :
        partial.append(letters[element][i])
        # backtracking
        backtracking(digits, results, partial, index+1)
        partial.pop()
    return results

def letterCombinations(digits):
    return backtracking(digits, [], [], 0)    


digits = "23"
print(letterCombinations(digits))
        