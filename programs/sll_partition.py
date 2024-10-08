# in a sll make a partition to around a value x. All nodes less than x  come before that all nodes equal or greater to x
# the x value can appear any where in the right partition. x not needs to appear in the middle, just in right partition.

from single_linked_lists import Node


def partition(h: Node, x: int) -> Node:     # this method creates 2 sll, 1 is fot the lower number 2 for the greater number
    less_nodes = Node(0)
    head_less = less_nodes
    great_nodes = Node(0)
    head_great = great_nodes

    while h:
        if h.data < x:
            less_nodes.next = h
            less_nodes = less_nodes.next
        else:
            great_nodes.next = h
            great_nodes = great_nodes.next

        h = h.next

    # then conect the two sll
    # the last node in less_nodes point to the first node in great_nodes, the last node in great_nodes point to None
    less_nodes.next = head_great.next
    great_nodes.next = None
    return head_less.next

h = Node.list_builder()
x = int(input("Which element wants to be the partition reference: "))

print(h)
print(partition(h, x))