# You are given a binary tree in which each node  contain an integer vale (positive or negative). Design an algorithm 
# to count the number of paths that sum a given value. The path doesn't need to start or end in root or left.
# it must go only downwrads, traveling from parent to child 
from binary_tree_base import Node



def path_with_sum(sub_a: Node, n: int, acc: int, paths) -> int:    # check if a sum is found in a tree
    # stop
    if sub_a == None :
        print("fin de nodo", paths)
        return paths
    # case base
    print("last", sub_a.data, paths, "acum", acc+sub_a.data)
    if acc + sub_a.data == n and acc != sub_a.data :        # if n is found it in a sum of nodes not only in a node
        paths += 1
        print("encontrado", sub_a.data, paths)
    # recursion
    paths = path_with_sum(sub_a.left, n, acc + sub_a.data , paths) 
    paths = path_with_sum(sub_a.right, n, acc + sub_a.data, paths)
    return paths
    

def walk_through(a: Node, n: int, paths: int) -> int:    # send every node to check as a tree
    # stop
    if a == None:
        return paths
    #operation
    
    print("mandar Nodo", a.data, "paths:", paths)
    paths =+  path_with_sum(a, n, 0, paths)
    # recursion
    walk_through(a.left, n, paths)
    walk_through(a.right, n, paths)
    #print("mandar 2",  a.data, "paths:", paths)
    paths += path_with_sum(a, n, 0, paths)
    return paths

def how_many_paths(a: Node, n: int) -> int:
    return walk_through(a, n, 0)    


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


paths = 0
#path_with_sum(root,30, 0)
print("begin")
print(how_many_paths(root, 15))

a = [root]
visited_nodes = []
Node.bfs_print(root, visited_nodes, a)
