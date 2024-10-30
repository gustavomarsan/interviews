"""
https://leetcode.com/problems/symmetric-tree/submissions/1437712060/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

from binary_tree_base import Node

def is_mirror(a: Node, b: Node) -> bool:
    # stop
    if a == None and b == None :
        return True
    # base case
    if a == None or b == None :
        return False
    # base case + recursion
    return a.data == b.data and is_mirror(a.left, b.right) and is_mirror(a.right, b.left) 


def is_symetrical(a: Node) -> bool:
    if a == None:
        return True
    return is_mirror(a.left, a.right)


root = Node(None)                                       #             1
root.data = 1                                           #         2        2
root.left = Node(2)                                     #       3   4    4    3   
root.left.left = Node(3)                                #                *
root.left.right = Node(4)                               #
root.right = Node(2)                                    #
root.right.right = Node(3)                              #
root.right.left = Node(4)                               #

a = [root]
visited_nodes = []
Node.bfs_print(root, visited_nodes, a)
print(is_symetrical(root))
