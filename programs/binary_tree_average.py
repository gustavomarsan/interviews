"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
637. Average of Levels in Binary Tree
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
Note: BFS
"""
from binary_tree_base import Node

def calculate(list, result) :
    new_list = []
    count = 0
    sum = 0
    while list :
        element = list.pop()
        if element == None :
            continue
        count += 1
        sum += element.data
        new_list.append(element.left) 
        new_list.append(element.right) 
    if new_list :
        prom = sum/count
        result.append(prom)
        calculate( new_list, result)
    else : 
        return result

    return result

def averageOfLevels(root):
    return calculate([root], [])
    
a = Node(2)
a.left = Node(4)
a.right = Node(6)
a.left.left = Node(8)
a.right.right = Node(9)   

print(averageOfLevels(a))
