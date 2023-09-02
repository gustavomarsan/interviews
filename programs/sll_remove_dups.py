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

    def RemDups(self):
        p1 = self.head  # p1 is ponter 1
        while p1.next:
            p2 = p1  # p2 is ponter 2
            while p2.next:
                if p1.data == p2.next.data:
                    if p2.next.next == None:
                        p2.next = None
                        break
                    else:
                        p2.next = p2.next.next
                        continue
                p2 = p2.next

            p1 = p1.next


# Create a single linked list
L = SingleLinkedList()
n0 = Node(1)
L.head = n0
n1 = Node(5)
n0.next = n1
n2 = Node(1)
n1.next = n2
n3 = Node(9)
n2.next = n3
n4 = Node(2)
n3.next = n4
n5 = Node(3)
n4.next = n5
n6 = Node(7)
n5.next = n6
n7 = Node(8)
n6.next = n7
n8 = Node(14)
n7.next = n8
n9 = Node(15)
n8.next = n9

print("Original linked list")
L.display()

L.RemDups()
L.display()
