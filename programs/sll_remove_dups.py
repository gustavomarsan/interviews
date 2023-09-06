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

    def RemDups(self):
        p1 = self.head  # p1 is ponter 1
        while p1.next:
            p2 = p1  # p2 is ponter 2
            while p2.next:
                if p1.data == p2.next.data:
                    if p2.next.next == None:
                        p2.next = None  # p2
                        break
                    else:
                        p2.next = p2.next.next
                        continue
                p2 = p2.next

            # Maybe when loop while p1.next began, p1.next had some value and after change to None. Validate
            if p1.next != None:
                p1 = p1.next


n = Node(input("Head: "))
h = n
h.head = n
for i in range(int(input("How many extra nodes? "))):
    nn = Node(input("Next node: "))
    n.next = nn
    n = n.next

h.display()
h.RemDups()
h.display()
