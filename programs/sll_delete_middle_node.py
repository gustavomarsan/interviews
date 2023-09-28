# in a single linked list delete a node in de middle, not the first, not de last, not necesary the exact middle
# You only receive the Node to delete, not de sll


from single_linked_lists import Node


# I have not element before I want to delete, I will replace values with next values  and delete next
def delete_element(element: Node):
    print("Hola")
    element.data = element.next.data
    element.next = element.next.next


h = Node.list_builder()
print(h)

k = int(input("Which element in the middle do You want to delete?: "))

found = 0
n = h
# Search element to delete
while n and n.next:
    # this if checks is next.data element is equal to element to delete and
    # n.next.next  validation is because the last element can´t be deleted
    if n.next.data == k and n.next.next:
        element = n.next
        found = 1
        break  # found the element to delete and break
    n = n.next

if found == 0:
    print("element not found in de middle")

else:
    delete_element(element)
    print(h)
