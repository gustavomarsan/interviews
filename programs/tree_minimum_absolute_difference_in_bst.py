"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.data <= 105

"""

from binary_search_tree import Node


def dfs(root: Node, diff):  
    if root == None:        #exit condition
        return
    
    dfs(root.left, diff)    #go left first
    if root.data - diff[1] < diff[0]:
        diff[0] = root.data - diff[1] 
    diff[1] = root.data
    dfs(root.right, diff)   #go right last

def getMinimumDifference(root: Node) -> int:
    # read the tree in-order and keep track of the previous number and minimum difference
    diff = [10**5, -10**5]      # diff[min_diff, prev_number]
    dfs(root, diff)             # recursive in-order traversal

    return diff[0]


        

root = Node(None)                                       #             1
root.data = 6                                           #         2        8
root.left = Node(2)                                     #       0   4    7    9   
root.left.left = Node(0)                                #          3 5    
root.left.right = Node(4)                               #
root.left.right.left = Node(3)                          #
root.left.right.right = Node(5)                         #
root.right = Node(8)                                    #
root.right.left = Node(7)            
root.right.right = Node(9)                              #

h= getMinimumDifference(root)
print("get minimum difference", h)
