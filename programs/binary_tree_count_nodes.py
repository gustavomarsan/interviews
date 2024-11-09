"""
https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150
222. Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.
Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:
Input: root = []
Output: 0
Example 3:
Input: root = [1]
Output: 1
Note : if left depth == right depth the tree is full complete then nodes = 2 ** depth -1
else count nodes by recursevely
"""
from binary_tree_base import Node


def sum_root(child: Node)-> int :
	# stop
    if not child :
        return 0
    # recursivity
    return 1 + sum_root(child.left) + sum_root(child.right)
    
def left_depth(root: Node)-> int :
    # stop
    if not root :
        return 0
    # recursivity
    return 1 + left_depth(root.left)
            
def right_depth(root: Node)-> int:
    # stop
    if not root :
        return 0
    # recursivity
    return 1 + right_depth(root.right)
            
def countNodes(root: Node)-> int:
    # if root is full and complete
    r = right_depth(root) 
    l = left_depth(root) 
    if root and r == l :
        return 2 ** r -1
    # else if root is not full and complete
    return sum_root(root)


a = Node(2)
a.left = Node(4)
a.right = Node(6)
a.left.left = Node(8)
a.left.right = Node(9)   
a.right.left = Node(10)

print(countNodes(a))