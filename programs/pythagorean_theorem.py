"""
Given a list of integers, return the first trio a, b, c, where a^2 + b^2 = c^2
The list contains duplicates, a, b, c should be different numbers
Input: [1, 2, 3, 4, 5]

my_dict = {1:1, 2:1, 3:1, 4:1, 5:1}
Output: (3, 4, 5)

Input: [2, 2, ] 
output: (1, 0, 1)

Input: [1, 0]
output: None
"""
import math 

def pythagorean(numbers: list[int])-> tuple:
	my_dict = {} 
	for num in numbers:
		my_dict[num] = my_dict.get(num, 0) + 1
	for i in range(len(numbers)-1):
		my_dict[numbers[i]] -= 1
		for j in range(i +1 , len(numbers)):
			my_dict[numbers[j]] -= 1
			c = math.sqrt(numbers[i]*numbers[i] + numbers[j]*numbers[j])
			if c == int(c):
				c = int(c)
				if c in my_dict and my_dict[c] != 0:
					return numbers[i], numbers[j], c
				if -c in my_dict and my_dict[-c] != 0:
					return numbers[i], numbers[j], -c
			my_dict[numbers[j]] += 1
		my_dict[numbers[i]] += 1
	return None

numbers = [1, 2, 3, 4, 5]
print(pythagorean(numbers))