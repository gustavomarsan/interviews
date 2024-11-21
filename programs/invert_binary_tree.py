"""
https://leetcode.com/problems/invert-binary-tree/
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
***Note:  read in pre-order and switch children
"""
from binary_tree_base import Node

def invert_child(root: Node) :
    if not root or  (not root.left and not root.right) :
        return
    root.left, root.right = root.right, root.left
    invert_child(root.left)
    invert_child(root.right)

def invertTree(root: Node):
    invert_child(root)
    return root

root = Node(None)                                       #             1
root.data = 1                                           #         2        5
root.left = Node(2)                                     #       3   4    6    7
root.left.left = Node(3)                                #                *
root.left.right = Node(4)                               #
root.right = Node(5)                                    #
root.right.right = Node(7)                              #
root.right.left = Node(6)            
  
print(root)        
invertTree(root)
print(root)        