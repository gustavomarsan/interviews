# in a sll make a partition to around a value x. All nodes less than x  come before that all nodes equal or greater to x
# the x value can appear any where in the right partition. x not needs to apear in the middle, just in right partition.
from single_linked_lists import Node

h = Node(None)
h = h.list_builder()
h.display()

x = int(input("Which element wants to be the partition reference: "))

p1 = h.head  # p1 = pointer 1

while p1.next:  # p1 walk sll
    if p1.data < x:
        p1 = p1.next
        continue
    p2 = p1.next  # p2 = poniter 1
    while p2:  # p2 walk sll
        # compare p1 and p2 and if necesary switch them
        if p2.data < p1.data and p2.data < x:
            temp = p1.data
            p1.data = p2.data
            p2.data = temp
            break
        if p2.next:
            p2 = p2.next
        else:
            break
    p1 = p1.next

h.display()
