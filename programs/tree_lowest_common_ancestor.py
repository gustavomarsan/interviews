from binary_search_tree import Node


def lowestCommonAncestor(root: Node, p: Node, q: Node) -> Node:
    while root:
        if p.data < root.data and q.data < root.data:
            root = root.left
        elif p.data > root.data and q.data > root.data:
            root = root.right
        else:
            return root
        

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

h= lowestCommonAncestor(root, Node(2), Node(8))
print("lowestCommonAncestor", h.data)
