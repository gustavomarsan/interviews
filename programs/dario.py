from single_linked_lists import Node


def add(n1: Node, n2: Node, prev: Node) -> int:
    if n1 is None or n2 is None:
        return 0

    curr = Node(0)
    prev.next = curr
    r = n1.data + n2.data + add(n1.next, n2.next, curr)
    curr.data = r % 10
    return r // 10


def add_zero(node: Node) -> Node:
    new = Node(0)
    new.next = node
    return new


def sum_lists(a: Node, b: Node) -> Node:
    n = a
    m = b

    while n and m:
        n, m = n.next, m.next

    if n is None:
        n = m
        temp = a
        a = b
        b = temp

    while n:
        b = add_zero(b)
        n = n.next

    a = add_zero(a)
    b = add_zero(b)
    result = Node(0)

    add(a, b, result)

    result = result.next
    if result.data == 0:
        return result.next
    return result


a = Node.list_builder()
b = Node.list_builder()

print(sum_lists(a, b))
