"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150
103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
              3
        9         20
  
                15   7
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Note: BFS but one level orderes left-right, next level ordered right-left 
"""
from collections import deque
from binary_tree_base import Node

def levels(level: deque, results: list, left: bool)-> list[list[int]] :
    partial = deque([])
    new_level = deque([])
    while level :
        element = level.popleft()
        if not element :
            continue
        new_level.append(element.left)
        new_level.append(element.right)
        if left :                               # insertiion mode for values changes every loop depends on left
            partial.append(element.data)
        else :
            partial.appendleft(element.data)
    if partial :
        results.append([item for item in partial])
    if new_level and left :
        levels(new_level, results, False)           # last param is for checking value insertion order
    if new_level and not left :
        levels(new_level, results, True)            # last param is for checking value insertion order
    return results
    
def zigzagLevelOrder(root: Node):
        return levels(deque([root]), [], True)  	# last param is for checking value insertion order

a = Node(2)
a.left = Node(4)
a.right = Node(6)
a.left.left = Node(8)
a.left.right = Node(9)   
a.right.left = Node(10)
print(zigzagLevelOrder(a))