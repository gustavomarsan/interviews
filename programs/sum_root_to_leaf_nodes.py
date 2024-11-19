"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/
129. Sum Root to Leaf Numbers
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.
Example 1:
                1
              2   3
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:
             4
          9     0
        5   1
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""
from binary_tree_base import Node

def pre_order(root, digits) :
    global acum
    if not root :
        return
    digits += str(root.data)
    pre_order(root.left, digits)
    pre_order(root.right, digits)
    if not root.left and not root.right :
        acum += int(digits)

def sumNumbers(root):
    global acum
    acum = 0
    pre_order(root, " ")
    return acum
        
root = Node(None)                                       #             1
root.data = 1                                           #         2        2
root.left = Node(2)                                     #       3   4    8      
root.left.left = Node(3)                                #                *
root.left.right = Node(4)                               #
root.right = Node(2)                                    #
root.right.left = Node(8)            
  
print(sumNumbers(root))