# Sum lists forward order (page 95. 2.5)
# input 2 sll exem. (6 -> 1 -> 7)  (2 -> 9 -> 5)   its equal to 617+295 = 912
# return the sum as a sll ( 9 -> 1 -> 2)

from single_linked_lists import Node


def sum_one_ten(a: Node, b: Node, is_first: bool = False) -> Node:
    if a is None:
        return None

    node = Node(a.data + b.data, sum_one_ten(a.next, b.next))

    if node.next is not None and node.next.data > 9:
        node.data += 1
        node.next.data -= 10

    if is_first and node.data > 9:
        node.data -= 10
        return Node(1, node)
    return node


def sum_nodes(a: Node, b: Node):
    head_a = a
    head_b = b

    while a or b:  # fill 0s in smaller sll
        if a:
            a = a.next
        else:
            temp = head_a
            head_a = Node(0)
            head_a.next = temp

        if b:
            b = b.next
        else:
            temp = head_b
            head_b = Node(0)
            head_b.next = temp

    return sum_one_ten(head_a, head_b, True)


a = Node.list_builder()
b = Node.list_builder()

print(sum_nodes(a, b))
