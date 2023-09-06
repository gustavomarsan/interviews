# In a single linked list find the kth elemment from the last


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

k = int(input("Kth element to find from the last: "))

p1 = h.head  # p1 is ponter 1
p2 = p1

for n in range(k):
    p2 = p2.next

while p2.next:
    p1 = p1.next
    p2 = p2.next

print(p1.data)
