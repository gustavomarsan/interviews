# given a tree, check if is a BST  (all node on the left are lower and all nodes on the rifght are graeter)

from binary_tree_base import Node
from collections import deque


def left_side(a, value) -> bool :
    if a == None:
        return
    queue = deque([a])
    while queue:
        next = queue.popleft()
        if next == None:
            continue
        if next.left :
            queue.append(next.left)
        if next.right :
            queue.append(next.right)
        if next.data > value:
            return False
    return True

def right_side(a, value) -> bool :
    
    if a == None:
        return
    queue = deque([a])
    while queue:
        next = queue.popleft()
        if next == None:
            continue
        if next.left :
            queue.append(next.left)
        if next.right :
            queue.append(next.right)
        if next.data < value:
            return False
    return True

   
    
def checkBST(root) -> bool:
    if root == None:
        return
    checkBST(root.left)
    checkBST(root.right)
    if left_side(root.left, root.data) and right_side(root.right, root.data):
        return "Yes"
    else:
        return "No"
    
    

root = Node(None)
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
#Node.insert(13, root)
#Node.insert(18, root)
#Node.insert(23, root)
#Node.insert(27, root)

#root.right.right.left.data = 2


root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)


a = [root]
visited_nodes = []
Node.bfs_print(root, visited_nodes, a)

numbers = []
print("Metodo BSF:",checkBST(root))

