"""""
We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.
Given a binary tree t, find the sum of all the numbers encoded in it.
                                r    218
        1                            1
     0    4                         / \
   3  1                        r  204  14
                                 0   4
                                / \
                            r 103 101
                                3  1 

the output should be
solution(t) = 218.
There are 3 numbers encoded in this tree:

Path 1->0->3 encodes 103
Path 1->0->1 encodes 101
Path 1->4 encodes 14
and their sum is 103 + 101 + 14 = 218.

O(n*n*l)
"""

from binary_tree_base import Node

def sum_paths(a: Node, acc: int) -> int:
    # stop
    if a == None :
        return 0
    acc += a.data
    # base case
    if a.left == None and a.right == None:
        return acc
    # recursion
    return sum_paths(a.left, acc*10) + sum_paths(a.right, acc*10)
     

def sum_leaves(a: Node)-> int:
 	return sum_paths(a, 0)
  
  
root = Node(None)                                       #             1
root.data = 1                                           #         2        2
root.left = Node(2)                                     #       3   4    8    3   
root.left.left = Node(3)                                #                *
root.left.right = Node(4)                               #
root.right = Node(2)                                    #
root.right.right = Node(3)                              #
root.right.left = Node(8)                               #

print(sum_leaves(root))