"""
https://leetcode.com/problems/validate-binary-search-tree/
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Input: root = [2,1,3]
Output: true
Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4. 
Note : By reading DFS in order and comparing if previous element is lower than current
"""
from binary_tree_base import Node

def in_order(root):
    global prev, is_valid
    if not is_valid or not root :
        return 
    in_order(root.left)
    if prev >= root.data :
        is_valid = False
        return 
    prev = root.data
    in_order(root.right)
    
def isValidBST(root):
    global prev, is_valid
    prev = float("-inf")
    is_valid = True
    in_order(root)
    return is_valid

root = Node(None)                                       #             100
root.data = 100                                         #         70        200
root.left = Node(70)                                    #       50   80   140   231   
root.left.left = Node(50)                               #                *
root.left.right = Node(80)                              #
root.right = Node(200)                                  #
root.right.right = Node(231)                            #
root.right.left = Node(140)            

print(isValidBST(root))