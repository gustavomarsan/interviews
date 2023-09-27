# In a single linked list find the kth elemment from the last,  last element is 0

from single_linked_lists import Node


def find_element(k: int, h: Node):
    p1 = h  # p1 is ponter 1
    p2 = p1

    for n in range(k):  # p2 walks k elements to get diference k vs. p1
        p2 = p2.next

    while p2.next:  # when p2 is in last element, p1 is in kth element from the last
        p1 = p1.next
        p2 = p2.next

    return p1.data


h = Node.list_builder()
print(h)

k = int(input("Kth element to find from the last: "))

print(find_element(k, h))
