"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:
Input: root = [1,null,2]
Output: 2
Constraints:
The number of nodes in the tree is in the range [0, 104].
"""

from binary_search_tree import Node

def depth(root) :
    if root == None :
        return 0
    		
    return  1 + max(depth(root.left), depth(root.right) )
		
def maxDepth(root):
    return depth(root) 

root = Node(None)                                       #             1
root.data = 1                                           #         2        2
root.left = Node(2)                                     #       3   4    4    3   
root.left.left = Node(3)                                #                *
root.left.right = Node(4)                               #
root.right = Node(2)                                    #
root.right.right = Node(3)                              #
root.right.left = Node(4)            
  
print(maxDepth(root))