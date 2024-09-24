""" given a complete tree print it bt in the odd number row print * instead the number

a:       1                      result = 1
     2      3                            **
   4   5   6  7                          4567
"""
from collections import deque
from binary_tree_base import Node

def print_christmas_tree(a: Node) -> None :
    d = deque([(a, 0)])
    prev_row = 0
    while len(d) > 0 :          # exit
        # operation       
        root, row = d.popleft()
        if prev_row != row :    # if row changed then change the line to print
            print("")
            prev_row = row  
        if row % 2 == 0 :
            print(root.data, end=" ")
        else :
            print("*", end= " ")
        # recursion 
        if root.left != None :
            d.append((root.left, row+1))
        if root.right != None : 
            d.append((root.right, row+1))
        
    print("")

root = Node(None)
Node.insert(10, root)
Node.insert(5, root)
Node.insert(20, root)
Node.insert(3, root)
Node.insert(8, root)
Node.insert(15, root)
Node.insert(25, root)
Node.insert(1, root)
Node.insert(4, root)
Node.insert(7, root)
Node.insert(9, root)
Node.insert(13, root)
Node.insert(18, root)
Node.insert(23, root)
Node.insert(27, root)

a = [root]
visited_nodes = []
Node.bfs_print(root, visited_nodes, a)
print_christmas_tree(root)

print("tree is balanced:", Node.is_balanced(root))


