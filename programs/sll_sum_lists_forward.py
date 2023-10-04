# Sum lists forward order (page 95. 2.5)
# input 2 sll exem. (6 -> 1 -> 7)  (2 -> 9 -> 5)   its equal to 617+295 = 912
# return the sum as a sll ( 9 -> 1 -> 2)

from single_linked_lists import Node


def sum_nodes(a: Node, b: Node):
    head_a = a
    head_b = b
    len_a = 0
    len_b = 0

    # compare len of the 2 sll
    while a or b:
        if a:
            a = a.next
            len_a += 1
        if b:
            b = b.next
            len_b += 1

    # add 0 to the smaller sll
    if (len_a - len_b) < 0:
        for n in range(len_b - len_a):
            temp = head_a
            head_a = Node(0)
            head_a.next = temp

    if (len_a - len_b) > 0:
        for n in range(len_a - len_b):
            temp = head_b
            head_b = Node(0)
            head_b.next = temp

    a = head_a
    b = head_b

    print("Fill 0s")
    print(a)
    print(b)

    head = Node(0)
    resul = head
    ten = 0
    while a or ten:
        sum = a.data + b.data + ten
        ten = 0
        if sum > 9:
            sum -= 10
            ten = 1
        new_node = Node(sum)
        resul.next = new_node
        resul = resul.next
        a = a.next
        b = b.next

    return head.next


a = Node.list_builder()
b = Node.list_builder()

print(a)
print(b)
print(sum_nodes(a, b))
