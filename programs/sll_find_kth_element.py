# In a single linked list find the kth elemment from the last,  last element is 0

from single_linked_lists import Node


def find_element(k: int, h: Node) :
    if h == None:
        return "Single linked list is empty"

    p1 = h  # p1 is ponter 1
    p2 = p1

    total_nodes = 0
    while p2 and total_nodes < k:  # p2 walks k steps to get diference betwen p1 and p2
        p2 = p2.next
        total_nodes += 1
        if p2 == None and total_nodes <= k:  # validate len of sll vs k
            print(f"ERROR, List has only {total_nodes} elements")
            return f"List has not {k+1} elements"

    while p2.next:  # when p2 is in last element, p1 is in kth element from the last, because the diference betwen p1 y p2 is k steps
        p1 = p1.next
        p2 = p2.next

    return p1.data      # p1 is now in kth element from teh last


h = Node.list_builder()
print(h)

k = int(input("Kth element to find from the last: "))
print(find_element(k, h))
