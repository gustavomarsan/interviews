"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' dataues. (i.e., from left to right, 
level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
"""

from collections import deque
from binary_search_tree import Node

def walk_child(a) :
	partial = []
	b = deque([])
	while a :
		node = a.popleft()
		if node.left :
			b.append(node.left)
			partial.append(node.left.data)
		if node.right :
			b.append(node.right)
			partial.append(node.right.data)
	return partial, b
	
def levelOrder(root):
	if root == None :
		return []
	results = [[root.data]]
	a = deque([root])
	while a :
		partial, a = walk_child(a)
		if partial :
			results.append(partial)
	return results

root = Node(None)
Node.insert(10, root)
Node.insert(5, root)
Node.insert(20, root)
Node.insert(3, root)
Node.insert(8, root)
Node.insert(15, root)
Node.insert(25, root)
Node.insert(1, root)
Node.insert(4, root)
Node.insert(7, root)
Node.insert(9, root)
Node.insert(13, root)
Node.insert(18, root)
Node.insert(23, root)
Node.insert(27, root)

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(6)
print(levelOrder(root))
