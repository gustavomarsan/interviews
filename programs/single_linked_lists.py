class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, " -->", end="  ")
                temp = temp.next
            print()


L = SingleLinkedList()
n = Node(10)
L.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
print("Original linked list")
L.display()


# insert a node in the begining
new = Node(5)
new.next = L.head
L.head = new

print("Insert node in the begining linked list")
L.display()

# insert a node in the begining
last = Node(100)
temp = L.head
while temp.next:
    temp = temp.next
temp.next = last
print("Insert node in the end linked list")
L.display()

# insert a node in 3rd place
middle = Node(25)
temp = L.head
for i in range(3 - 1):
    temp = temp.next
middle.next = temp.next
temp.next = middle
print("Insert node in the 3er place of linked list")
L.display()
