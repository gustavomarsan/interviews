"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
107. Binary Tree Level Order Traversal II
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, 
level by level from leaf to root).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
** Note: 2 options   **
"""

from binary_tree_base import Node
from collections import deque

def fill_levels(level: deque, results: list[int]) -> list[list[int]]:
    # exit
    if not level :
        return
    next_level = deque()
    list_level = []
    while level :
        element = level.popleft()
        list_level.append(element.data)
        if element.left :
            next_level.append(element.left)
        if element.right :
            next_level.append(element.right)
    # recursion    
    fill_levels(next_level, results)       # first recursive
    results.append(list_level)              # then add level to result, it makes bottom to up
    return results


def level_order_bottom(root: Node) -> list[list[int]]:          #option 1, go to recursive funtion (fill_result) for each level
    if not root :
        return []
    
    return fill_levels(deque([root]), [])


def level_order_bottom2(root: Node) -> list[list[int]]: #option 2 do it in the same function storing (root, level) in a queue
    if not root :                                       # and the results is a dequeu stored by appendleft
        return []
    last_level = 1
    results = deque()
    list_levels = []
    queue = deque([(root, 1)])
    while queue :
        element, level = queue.popleft()
        if level != last_level :        
            last_level = level
            results.appendleft(list_levels)     # whwn lele changes update results
            list_levels = []
        list_levels.append(element.data)
        if element.left :
            queue.append((element.left, level+1))
        if element.right :
            queue.append((element.right, level+1))
    results.appendleft(list_levels) # append the last list_levels
    return list(results)


    





root = Node(None)                                       #             1
root.data = 1                                           #         2        7
root.left = Node(2)                                     #       3   4    6    8   
root.left.left = Node(3)                                #            5   
root.left.right = Node(4)                               #
root.right = Node(7)                                    #
root.right.right = Node(8)                              #
root.right.left = Node(6)            
#root.left.right.right=Node(5)

print(level_order_bottom(root))
print(level_order_bottom2(root))