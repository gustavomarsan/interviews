from single_linked_lists import Node

class Node_tree:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return (
            str(self.data)
            + "( <--  "
            + str(self.left)
            + "  --> "
            + str(self.right)
            + " )"
        )


    def insert(data: int, root) :
            if root.data == None:  # if tree is empty
                root.data = data
                return      

            if data < root.data :
                if root.left != None :
                    Node_tree.insert(data, root.left)
                else: 
                    root.left = Node_tree(data)  
                    return

            if data > root.data :
                if root.right != None :
                    Node_tree.insert(data, root.right)
                else : 
                    root.right = Node_tree(data)
                    return
                


def list_of_depths(a: Node_tree, depths: list[Node], level)-> list[list[Node_tree]]:
    # stop
    if a == None :
        return 
    # opreration
    if len(depths) > level :
        p2 = depths[level]                      #pointer 2 to walk in linked list and get de last node
        while p2.next != None :
            p2 = p2.next
        p2.next = Node(a.data)
    if len(depths) == level :
        depths.append(Node(a.data))
    # recursion
    list_of_depths(a.left, depths, level+1)
    list_of_depths(a.right, depths, level+1)
    return depths

def bfs_print(root)-> list[int] :       # Breath First Search
        if not root :
            return
        if a[0].left != None:
            a.append(root.left)
        if a[0].right != None:
            a.append(root.right)
        visited_nodes.append(a[0].data)
        a.pop(0)

        if len(a) > 0 :
            bfs_print(a[0])
        else :
            print("BFS  --> ",visited_nodes)

                
root = Node_tree(None)
Node_tree.insert(80, root)
Node_tree.insert(150, root)
Node_tree.insert(145, root)
Node_tree.insert(20, root)
Node_tree.insert(40, root)
Node_tree.insert(10, root)
Node_tree.insert(45, root)
Node_tree.insert(50, root)
Node_tree.insert(5, root)
Node_tree.insert(35, root)
Node_tree.insert(55, root)
Node_tree.insert(160, root)
Node_tree.insert(170, root)
Node_tree.insert(180, root)
Node_tree.insert(140, root)
Node_tree.insert(135, root)

a = [root]
visited_nodes = []
bfs_print(root)


depths = []
level = 0

tree_list = list_of_depths(root, depths, 0)
print(type(tree_list))
for item in tree_list :
    print(item)
