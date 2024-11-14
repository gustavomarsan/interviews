"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values 
of the nodes in the tree.
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
*** Note: By doind DFS in order and counting until kth element, usinf global variables. In leet code uses Class variables.
"""
from binary_tree_base import Node
def count_nodes(root: Node)-> int :
    global kth, count, finished, value
    if finished or not root :
        return
    if not finished :                   # if finished stop DFS
        count_nodes(root.left)
        count += 1
        if count == kth :
            value = root.data
            finished = True
    if not finished :                    # if finished stop DFS
        count_nodes(root.right)

def kthSmallest(root: Node, k: int)-> int :
    global kth, count, finished, value
    kth = k
    count = 0
    value = 0
    finished = False
    count_nodes(root)
    return value
    

root = Node(None)                                       #             100
root.data = 100                                         #         70        200
root.left = Node(70)                                    #       50   80   140   231   
root.left.left = Node(50)                               #                *
root.left.right = Node(80)                              #
root.right = Node(200)                                  #
root.right.right = Node(231)                            #
root.right.left = Node(140)            

print(kthSmallest(root, 4))        