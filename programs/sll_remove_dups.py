from single_linked_lists import Node


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


for i in range(int(input("How many nodes to dups? "))):
    nn = Node(input(f"Node {i} : "))
    if i == 0:
        n = nn
        h = n
        h.head = n
    n.next = nn
    n = n.next

h.display()
RemDups(h)
h.display()
