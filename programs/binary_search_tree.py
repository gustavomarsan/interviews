tb = bool

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

    def insert(data: int, root):
        if root.data == None:  # if tree is empty
            root.data = data
            return root

        element = root
        grandfather = root
        father = root
        while True:
            if data > element.data:
                if element.right:
                    element = element.right
                    continue
                else:
                    element.right = Node(data)
                    break

            else:
                if element.left:
                    element = element.left
                    continue
                else:
                    element.left = Node(data)
                    break

        return root

    def find(data: int, root) -> bool:
        element = root
        while True:
            if element.data == data:
                return True
            if data > element.data:
                if element.right:
                    element = element.right
                    continue
                else:
                    return False

            else:
                if element.left:
                    element = element.left
                    continue
                else:
                    return False

    def delete(data: int, root):
        element = root
        if root.data == data:
            return "Element root can not be deleted"

        while True:
            if element.data == data:
                print("lo encontre", element.data)
                break
            if data > element.data:
                if element.right:
                    father = (element, "right")
                    element = element.right
                    continue
            else:
                if element.left:
                    father = (element, "left")
                    element = element.left
                    continue
        # if no child, direct delete
        if element.left == None and element.right == None:
            if father[1] == "left":
                father[0].left = None
            if father[1] == "right":
                father[0].right = None

            return root

        # if one child, delete and replace directly
        if element.left == None or element.right == None:
            if father[1] == "left":  # check if is father branch left or right
                if (
                    element.left != None
                ):  # connect father and child of the node to delete
                    father[0].left = element.left
                else:
                    father[0].left = element.right

            if father[1] == "right":  # check if is father branch left or right
                if (
                    element.right != None
                ):  # connect father and child of the node to delete
                    father[0].right = element.right
                else:
                    father[0].right = element.left
            return root

        # if two children, go to right child, find de left, left, left, leaf and substitute values and delete leaf
        if element.left != None and element.right != None:
            newvalue = element.right
            # if newvalue has no left child, only subtitute element node with new value node,
            if newvalue.left == None:
                element.data = newvalue.data
                if (
                    newvalue.right == None
                ):  # if newvalue has no right child the delete newvalue
                    element.right = None
                else:  # if newvalue has right chlid, this child will be chil of element
                    element.right = newvalue.right
                return root

            while newvalue.left != None:
                father = newvalue
                newvalue = newvalue.left

            element.data = newvalue.data
            if newvalue.right != None:
                father.left = newvalue.right
            else:
                father.left = None

            return root

    def height(root) -> int:
        if root is None:
            return -1
        return max(Node.height(root.left), Node.height(root.right)) + 1

    def is_balanced(root) -> bool:
        if abs(Node.height(root.left) - Node.height(root.right)) > 1:
            return False
        else : 
            return True
    
    def all_tree_balanced(root, tree_balance) -> bool:
        global tb
        if tree_balance == False or tb == False:
            return False
        else :
            print(root.data, " Is this branch balaced? ", Node.is_balanced(root))            
            if Node.is_balanced(root) == False :
                tb = False
                return False
            if root.left :
                Node.all_tree_balanced(root.left, tree_balance)
            if root.right and tb == True:
                Node.all_tree_balanced(root.right, tree_balance)
        if tb == False: 
            return False
        return  True
        



root = Node(None)
#root = Node.insert(80, root)
#root = Node.insert(150, root)
root = Node.insert(20, root)
root = Node.insert(40, root)
root = Node.insert(10, root)
root = Node.insert(45, root)
root = Node.insert(50, root)
root = Node.insert(5, root)
root = Node.insert(35, root)
#root = Node.insert(55, root)
#root = Node.insert(160, root)
#root = Node.insert(170, root)
#root = Node.insert(180, root)


print(root)
print("------")
root = Node.delete(40, root)
# root = Node.delete(8, root)
print(root)
# print("=======")
# root = Node.delete(20, root)

#print(Node.height(root))
#print(Node.is_balanced(root))
tb = True
print(Node.all_tree_balanced(root, True))
