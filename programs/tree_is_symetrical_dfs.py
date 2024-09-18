# check if a tree is symetrical with BFS

from collections import deque
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
root.left = Node(2)                                     #       3   4    5    3   
root.left.left = Node(3)                                #                *
root.left.right = Node(4)                               #
root.right = Node(2)                                    #
root.right.right = Node(3)                              #
root.right.left = Node(4)                               #

a = [root]
visited_nodes = []
Node.bfs_print(root, visited_nodes, a)
print(is_symetrical(root))
