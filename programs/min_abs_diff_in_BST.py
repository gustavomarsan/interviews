"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
530. Minimum Absolute Difference in BST
Example 1:
Input: root = [4,2,6,1,3]
Output: 1
Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 10**5
"""
from binary_tree_base import Node

def fill_list(root: Node, my_list: list[int])-> list[int] :
    if not root :
        return
    fill_list(root.left, my_list)
    my_list.append(root.data)
    fill_list(root.right, my_list)
    return my_list
    
def getMinimumDifference(root: Node)-> int:
    my_list = fill_list(root, [])
    min_diff = my_list[1] - my_list[0]
    for i in range(1, len(my_list)- 1) :
        min_diff = min(min_diff, (my_list[i+1]- my_list[i]))
    
    return min_diff
        
root = Node(None)                                       #             100
root.data = 100                                         #         70        200
root.left = Node(70)                                    #       50   80   140   231   
root.left.left = Node(50)                               #                *
root.left.right = Node(80)                              #
root.right = Node(200)                                  #
root.right.right = Node(231)                            #
root.right.left = Node(140)            

      
print(getMinimumDifference(root))   