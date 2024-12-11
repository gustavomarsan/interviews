# given a tree, check if is a BST  (all node on the left are lower and all nodes on the rifght are graeter)

from binary_tree_base import Node
from collections import deque

# support
# check all nodes which depends from this node using deque
def left_side(a, value) -> bool :
    if a == None:
        return True
    queue = deque([a])
    while queue:
        next = queue.popleft()
        if next == None:
            continue
        if next.data > value:
            return False
        if next.left :
            queue.append(next.left)
        if next.right :
            queue.append(next.right)
        
    return True
# support
# check all nodes which depends from this node using deque
def right_side(a, value) -> bool :
    
    if a == None:
        return True
    queue = deque([a])
    while queue:
        next = queue.popleft()
        if next == None:
            continue
        if next.data < value:
            return False
        if next.left :
            queue.append(next.left)
        if next.right :
            queue.append(next.right)
        
    return True
   
# by checking all nodes of left side to be lower and all nodes of right side to be greater in every node of the tree
# using a function to check lef and right children (walking through the tre in pre order traversal)
# main
def checkBST(root: Node) -> bool:       
    if root == None:
        return True
    if left_side(root.left, root.data) and right_side(root.right, root.data) :
        return checkBST(root.left) and checkBST(root.right)
    else :
        return False
    
    
# support    
def is_bst(root: Node, prev: list) :        
    # exit
    if not root :
        return True                         # while don't break rule that value > prev return True
    is_bst(root.left, prev)
    if root.data < prev[0]:
        return False
    prev[0] = root.data
    return is_bst(root.right, prev)

# by reading the tree in order traversal and checking if current value is greater than previous value. Previous inits in -inf
# prev is list[prev_val] it means prev[0] has the previous value
# main
def checkBST_2(root: Node) -> bool:
    return is_bst(root, [float('-inf')])     # send prev value in parameter as a list to be updated whatever recursion is
                                                                                                            # being doing 
            


#root = Node(None)
#Node.insert(10, root)
#Node.insert(5, root)
#Node.insert(20, root)
#Node.insert(3, root)
#Node.insert(8, root)
#Node.insert(15, root)
#Node.insert(25, root)
#Node.insert(1, root)
#Node.insert(4, root)
#Node.insert(7, root)
#Node.insert(9, root)
#Node.insert(17, root)
#Node.insert(18, root)
#Node.insert(23, root)
#Node.insert(27, root)

#root.right.right.left.data = 2


root = Node(10)
root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(8)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(25)


a = deque([root])
visited_nodes = []
print(Node.bfs_print(visited_nodes, a))

numbers = []
print("Metodo BSF:",checkBST(root))

print("Metodo BSF_2:",checkBST_2(root))

