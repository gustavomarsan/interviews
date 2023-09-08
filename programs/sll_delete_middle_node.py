# in a single linked list delete a node in de middle, not the first, not de last, not necesary the exact middle


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end="  ")
                if temp.next:
                    print("--->", end=" ")
                temp = temp.next
            print()


for i in range(int(input("How many nodes? "))):
    nn = Node(input(f"Node {i} : "))
    if i == 0:
        n = nn
        h = n
        h.head = n
    n.next = nn
    n = n.next


h.display()

k = input("Which element in the middle do You want to delete?: ")

n = h.head
while n.next:
    if n.next.data == k:
        n.next = n.next.next
    n = n.next

h.display()
