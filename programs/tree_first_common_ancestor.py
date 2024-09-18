# find the first common ancestor between given p and q numbers in a tree
# if p is in tree and not q, return p and viceversa 

from binary_search_tree import Node

def list_find(data: int, root) -> bool :
        global found
        global route
        # exit
        if root.data == None:                              # root is empty return False
            found = False
        route.append(root.data)
        if data == root.data :                              # data found in root.data, return True
            found = True
            return found
        # what to do and recursion
        if data < root.data and root.left != None:          #if is data is less than root.data check in left child
            list_find(data, root.left)
        elif data < root.data and root.left == None:        #if is data is less than root.data and no left child, not found 
            found = False
        elif data > root.data and root.right != None:       #if is data is greater than root.data and check in right child 
            list_find(data, root.right)
        elif data > root.data and root.right == None:       #if is data is greater than root.data and no right child, not found 
            found = False

        return  found


def first_common_ancestor(a:Node, p: int, q: int) :
    p_list, q_list = [],[]
    global route
    route = []
    global found
    found = False
    if list_find(p, root) :                 # check if p is in tree and return the list of parents
        p_list = route
    route = []
    found = False
    if list_find(q, root) :                 # check if p is in tree and return the list of parents
        q_list = route

    if len(p_list) > 0 and len(q_list) == 0 :   # if p or q are not in the tree de list_find function return an empty list
        return p

    if len(p_list) ==  0 and len(q_list) > 0 :
        return q

    for n in range(len(p_list)-1, -1, -1) :     # look up for a coincidences in the lists from back to front
        if (p_list[n]) in q_list :              # in this case both numbers are in the tree, tha last chance to be an ancester is root
            break
    return p_list[n]



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

p= 13
q = 23
print(first_common_ancestor(root, p, q))          # method I,  generates a list of parents (p, q) and compare both lists.
                                                # extra space 2 list ( 1 for each p and q) 
