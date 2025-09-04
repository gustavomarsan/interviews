from single_linked_lists import Node


def remove_duplicates(head: Node) -> None:
    p1 = head  # p1 is ponter 1
    while p1:
        while p1.next and p1.data == p1.next.data :
            p1.next = p1.next.next
        
        p1 = p1.next
        
    return head

h = Node.list_builder()
print(h)

remove_duplicates(h)
print(h)
