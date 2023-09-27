# Sum lists (page 95. 2.5)
# input 2 sll exem. (2 -> 1 -> 6)  (2 -> 5 -> 3)   its equal to 612+352 = 964
# return the sum as a sll ( 4 -> 6 -> 9)

from single_linked_lists import Node


def sum_nodes(a: Node, b: Node):
    print(a)
    print(b)

    head = Node(0)
    resul = head
    ten = 0
    while a:
        sum = a.data + b.data + ten
        if sum > 9:
            sum -= 10
            ten = 1
        else:
            ten = 0

        new_node = Node(sum)
        resul.next = new_node
        resul = resul.next
        if a.next:
            a = a.next
        else:
            if ten == 1:
                new_node = Node(1)
                resul.next = new_node

            break

    return head.next


a = Node.list_builder()
b = Node.list_builder()

s = sum_nodes(a, b)
print(s)
