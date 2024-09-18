from binary_tree_base import Node
    
def equals(a, b) -> bool :
        # stop
        if a == None and b == None :
            return True
        # case base
        if a == None or b == None :
            return False
        # case base and recursion
        return a.data == b.data and equals(a.left, b.left) and equals(a.right, b.right) 
        

            
            
tree_a = Node(None)
Node.insert(80, tree_a)
Node.insert(150, tree_a)
Node.insert(145, tree_a)
Node.insert(20, tree_a)
Node.insert(40, tree_a)
Node.insert(10, tree_a)
Node.insert(45, tree_a)
Node.insert(50, tree_a)
Node.insert(5, tree_a)
Node.insert(35, tree_a)
Node.insert(55, tree_a)
Node.insert(160, tree_a)
Node.insert(170, tree_a)
Node.insert(180, tree_a)
Node.insert(140, tree_a)
Node.insert(135, tree_a)

tree_b = Node(None)
Node.insert(80, tree_b)
Node.insert(150, tree_b)
Node.insert(145, tree_b)
Node.insert(20, tree_b)
Node.insert(40, tree_b)
Node.insert(10, tree_b)
Node.insert(45, tree_b)
Node.insert(50, tree_b)
Node.insert(5, tree_b)
Node.insert(35, tree_b)
Node.insert(55, tree_b)
Node.insert(160, tree_b)
Node.insert(170, tree_b)
Node.insert(180, tree_b)
Node.insert(140, tree_b)
Node.insert(135, tree_b)

a = [tree_a]
visited_nodes = []
Node.bfs_print(tree_a, visited_nodes, a)

a = [tree_b]
visited_nodes = []
Node.bfs_print(tree_b, visited_nodes, a)

print(equals(tree_a, tree_b))
    