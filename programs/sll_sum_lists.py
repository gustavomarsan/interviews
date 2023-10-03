# Sum lists (page 95. 2.5)
# input 2 sll exem. (2 -> 1 -> 6)  (2 -> 5 -> 3)   its equal to 612+352 = 964
# return the sum as a sll ( 4 -> 6 -> 9)

from single_linked_lists import Node


def sum_nodes(a: Node, b: Node):
    head = Node(0)
    resul = head
    ten = 0

    while a or b or ten:
        if a:
            value_a = a.data
        else:
            value_a = 0
        if b:
            value_b = b.data
        else:
            value_b = 0
        sum = value_a + value_b + ten
        ten = 0

        if sum > 9:
            sum -= 10
            ten = 1

        new_node = Node(sum)
        resul.next = new_node
        resul = resul.next

        if a:
            a = a.next
        if b:
            b = b.next

    return head.next


a = Node.list_builder()
b = Node.list_builder()

s = sum_nodes(a, b)
print(a)
print(b)
print(s)
