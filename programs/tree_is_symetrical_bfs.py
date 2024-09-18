# check if a tree is symetrical with BFS

from collections import deque
from binary_tree_base import Node

def is_symetrical(root: Node) -> bool:                # only one function
    if root == None:                                  #check first if is empty anits childs are None
        return True
    if root.left == None and root.right == None:
        return True
    if root.left == None or root.right == None:
        return False
    queue = deque([(root.left, root.right)])
    while queue :
        a, b = queue.popleft()
        if a == None and b == None :
            return True
        if a == None or b == None :
            return False
        if a.data != b.data :
            return False
        queue.append((a.left,b.right))
        queue.append((a.right, b.left))
    return True


root = Node(None)
root.data = 1
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(2)
root.right.right = Node(3)
root.right.left = Node(4)

a = [root]
visited_nodes = []
Node.bfs_print(root, visited_nodes, a)
print(is_symetrical(root))
