"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
example

        1
     |    |
     2    5
   |   |    |
   3   4    6

   1-> 2-> 3-> 4-> 5-6        Notice that in pre-order dfs left node became none, an right node became next 

Also  known as MORRIS TRAVERSAL
"""
from binary_tree_base import Node
    
def flatten(root):
    head = root
    while head :
        if head.left != None :
            runner = head.left
            while runner.right :
                runner = runner.right
            runner.right = head.right
            head.right = head.left
            head.left = None
        head = head.right

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.right = Node(6)

print(root)
flatten(root)
print(root)
     

        

