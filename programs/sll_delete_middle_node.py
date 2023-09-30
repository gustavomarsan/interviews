# in a single linked list delete a node in de middle, not the first, not de last, not necesary the exact middle
# You only receive the Node to delete, not de sll


from single_linked_lists import Node


# I have not element before I want to delete, I will replace values with next values and delete next node
def delete_element(element: Node):
    element.data = element.next.data
    element.next = element.next.next


h = Node.list_builder()
print(h)

k = int(input("Which element in the middle do You want to delete?: "))

found = False
n = h
# firs element can't be deleted
n = n.next
# Search element to delete
while n:
    # this if checks is next.data element is equal to element to delete and
    # n.next.next  validation is because the last element can´t be deleted
    if n.data == k and n.next is not None:
        delete_element(n)
        print(h)
        found = True
        break  # found the element to delete and break
    n = n.next

if not found:
    print("element not found in de middle")
