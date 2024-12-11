import random
from collections import deque

class Node:
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
                Node.insert(data, root.left)
            else: 
                root.left = Node(data)  
                return

        if data > root.data :
            if root.right != None :
                Node.insert(data, root.right)
            else : 
                root.right = Node(data)
                return
    
    def find(data: int, root) -> bool :
        global found
        # exit
        if root.data == None :                              # root is empty return False
            found = False
        if data == root.data :                              # data found in root.data, return True
            found = True
            return found
        # what to do and recursion
        if data < root.data and root.left != None:          #if is data is less than root.data check in left child
            Node.find(data, root.left)
        elif data < root.data and root.left == None:        #if is data is less than root.data and no left child, not found 
            found = False
        elif data > root.data and root.right != None:       #if is data is greater than root.data and check in right child 
            Node.find(data, root.right)
        elif data > root.data and root.right == None:       #if is data is greater than root.data and no right child, not found 
            found = False

        return  found

    def delete(data: int, root)-> None:
        #salida
        if root == None :
            return
        #operation        
        if root.data == data :                                        # found 
            print("encontrado", "data: ", root.data, "left child: ", root.left, "right child: ",root.right)
            if root.left == None and root.right == None :             # found and its a leaf node
                print("problema: eliminar nodo, padre.loquesea lo debe eliminar")                                   
                root.data = None
            if root.left != None and root.right == None :             # found and has only left child
                root = root.left
            if root.left == None and root.right != None :             # found and has only right child
                root.left = root.left.right
            if root.left != None and root.right != None :             # found and has two child children
                                                                      # check if there are grandchildren on the right side
                if root.right.left == None and root.right.right == None : # No grandchildren move it up the right chilf
                    root.data = root.right.data
                    root.right = None
                if root.right.left == None and root.right.right != None :    # right child has only right child move it up
                    print("yes", root.data, root.right.data)
                    root.data  = root.right.data
                    root.right = root.right.right
                if root.right.left != None:                            # if right child has left child seek for the lower
                    p2 = root.right
                    while p2.left.left != None :
                        p2 = p2.left
                    root.data = p2.left.data
                    p2.left = None

        #recursion                
        Node.delete(data, root.left)
        Node.delete(data, root.right)

        
    def height(root) -> int:
        if root is None:
            return -1
        return max(Node.height(root.left), Node.height(root.right)) + 1


    def col_number(root, n: int, numbers: list[int]) -> list[int] :
        if root == None :
            return numbers

        if n == 0 :
            numbers.append(root.data)

        Node.col_number(root.left, n -1, numbers)
        Node.col_number(root.right, n +1, numbers)

        return numbers

    def dfs_print(root) -> None:            # Deep First Search
        #if not root :
        #    return
        if root.left :
            Node.dfs_print(root.left)
        print(root.data, end = " ")
        if root.right :
            Node.dfs_print(root.right)

    def bfs_print(visited_nodes, a)-> list[int] :       # Breath First Search
        #exit
        if not a :
            return
        # action
        next = deque([])
        while a :
            element = a.popleft()
            if element.left != None:
                next.append(element.left)
            if element.right != None:
                next.append(element.right)
            visited_nodes.append(element.data)
        #recursion
        Node.bfs_print(visited_nodes, next)
        
        return visited_nodes

    def is_balanced(a) -> bool :
        # stop
        if a == None :
            return True
        # operation
        if abs(Node.height(a.left) - Node.height(a.right)) >  1 :
            return False
        # recursion
        return Node.is_balanced(a.left) and  Node.is_balanced(a.right)

def fill_numbers(a:Node)-> None:
    if a == None :
        return
    fill_numbers(a.left)
    all_num.append(a.data)
    fill_numbers(a.right)

def get_random(a: Node) -> Node :   # return a random node, put it in a list and selct a random number to equal possibilities
    global all_num
    all_num = []
    fill_numbers(a)
    number = (int(len(all_num)*(random.random())-.001))
    print(number)
    return all_num[number]


        

root = Node(None)
Node.insert(80, root)
Node.insert(150, root)
Node.insert(145, root)
Node.insert(20, root)
Node.insert(40, root)
Node.insert(10, root)
Node.insert(45, root)  
Node.insert(50, root)
Node.insert(5, root)
Node.insert(35, root)
Node.insert(55, root)
Node.insert(160, root)
Node.insert(170, root)
Node.insert(180, root)
Node.insert(140, root)
Node.insert(135, root)
print(root)


print("Height : ",Node.height(root))
#n = -2
#numbers = []
#print(f"Nodes in col = {n} :", Node.col_number(root, -n, numbers))

Node.dfs_print(root)
print(" ")

a = deque([root])
visited_nodes = []
print("bfs:", Node.bfs_print(visited_nodes, a))
print("Balanceado?:", Node.is_balanced(root))

print(get_random(root))
#print(Node.find(5, root))

#Node.delete(55, root)
#print(root)

# por resolver, como borrar nodo cuando el que borras es el ultimo 
