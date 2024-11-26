"""
https://leetcode.com/problems/path-sum/
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.
A leaf is a node with no children.
Example 1:                  *5
                        *4       8
                     *11       13  4
                   7   *2            1
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
*** Note :  similar solution as maximum depth by checking both sides (left and right with recursivity)
"""

from binary_tree_base import Node 

def hasPathSum(root: Node, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.data
    left_sum = hasPathSum(root.left, targetSum - root.data)
    right_sum = hasPathSum(root.right, targetSum - root.data)
    return left_sum or right_sum

root = Node(None)                                       #             1
root.data = 1                                           #         2        5
root.left = Node(2)                                     #       3   4    7    8   
root.left.left = Node(3)                                #                *
root.left.right = Node(4)                               #
root.right = Node(5)                                    #
root.right.right = Node(8)                              #
root.right.left = Node(7)            

print(hasPathSum(root, 7))
  