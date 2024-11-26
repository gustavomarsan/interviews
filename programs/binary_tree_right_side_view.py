"""
https://leetcode.com/problems/binary-tree-right-side-view/
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes 
you can see ordered from top to bottom.
Example 1:
                        1          <-
                    2       3      <-
                       5      4    <-
                    7              <-          1,3,4,7
Example 2:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 3:
Input: root = [1,null,3]
Output: [1,3]
Example 4:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
*** Note: bult by BFS, adding the children of the level to a new level and add the right value to result

"""
from binary_tree_base import Node
from collections import deque
def last_of_the_row(elements: deque[Node], results: list) :
    results.append(elements[-1].data)         #add to result the last value of the list of roots, stored from left to right
    new_elements = deque([])
    while elements :
        node = elements.popleft()
        # store all the children of the level of roots generating the next level of roots
        if node.left :
            new_elements.append(node.left)
        if node.right :
            new_elements.append(node.right)
    if new_elements :
        last_of_the_row(new_elements, results)          # send all the children to recursive process
    return results

def rightSideView(root: Node):
        if not root :
            return []
        return last_of_the_row(deque([root]), [])

root = Node(None)                                       #             1
root.data = 1                                           #         2        7
root.left = Node(2)                                     #       3   4    6    8   
root.left.left = Node(3)                                #            5   
root.left.right = Node(4)                               #
root.right = Node(7)                                    #
root.right.right = Node(8)                              #
root.right.left = Node(6)            
root.left.right.right=Node(5)
  
            
print(rightSideView(root))