from single_linked_lists import Node


def remove_duplicates(head: Node) -> None:
    p1 = head  # p1 is ponter 1
    while p1.next:
        p2 = p1  # p2 is ponter 2
        while p2.next:
            if p1.data == p2.next.data:
                if p2.next.next == None:
                    p2.next = None  # p2
                    break
                else:
                    p2.next = p2.next.next
                    continue
            p2 = p2.next

        # Maybe when loop while p1.next began, p1.next had some value and after change to None. Validate
        if p1.next != None:
            p1 = p1.next


h = Node.list_builder()
print(h)
remove_duplicates(h)
print(h)
