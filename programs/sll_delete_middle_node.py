# in a single linked list delete a node in de middle, not the first, not de last, not necesary the exact middle

from single_linked_lists import Node


h = Node(None)
h = h.list_builder()
h.display()

k = input("Which element in the middle do You want to delete?: ")

found = 0
n = h.head
while n.next:
    # this if checks is next.data element is equal to elenment to delete and
    # n.next.next  validation is because the last element can´t be deleted
    if n.next.data == k and n.next.next:
        n.next = n.next.next
        found = 1
        break  # found the element to delete and break
    n = n.next

if found == 0:
    print("element not found in de middle")
else:
    print("element found and deleted")

h.display()
