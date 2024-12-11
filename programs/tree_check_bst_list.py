# given a tree, check if is a BST  (all node on the left are lower and all nodes on the rifght are graeter)

from binary_tree_base import Node
from collections import deque



def fill_numbers(a: Node, numbers: list) -> None :         #create a list in order DFS
    if a == None :
        return
    
    fill_numbers(a.left, numbers)
    numbers.append(a.data)
    fill_numbers(a.right, numbers)
    return numbers

def check_bst(a: Node) -> bool:             # option 1. passing the numbers in order to a list and compare reviw rthe list 
    numbers = fill_numbers(a, [])                         # fill the list in order
    print(numbers)
    for n in range(len(numbers) -1) :    # check the list, if isn't ordered return False
        if numbers[n] >= numbers[n+1] :
            return False
    return True


        

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

#root.right.right.left.data = 11

a = deque([root])
visited_nodes = []
Node.bfs_print(visited_nodes, a)

numbers = []
print("Metodo list:",check_bst(root))

