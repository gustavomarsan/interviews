# Sum lists forward order (page 95. 2.5)
# input 2 sll exem. (6 -> 1 -> 7)  (2 -> 9 -> 5)   its equal to 617+295 = 912
# return the sum as a sll ( 9 -> 1 -> 2)

from single_linked_lists import Node


def sum_one_ten(a: Node, b: Node, result: Node):
    if a.next:
        sum_one_ten(a.next, b.next, result)

    new_node = Node(a.data + b.data + result.data)
    temp = result.next
    result.next = new_node
    new_node.next = temp
    if result.next.data > 9:  # manage the ten in result.head
        result.next.data -= 10
        result.data = 1
    else:
        result.data = 0
        return result.next
    return result


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

    head = Node(0)
    result = head

    return sum_one_ten(head_a, head_b, result)


a = Node.list_builder()
b = Node.list_builder()

print(sum_nodes(a, b))
