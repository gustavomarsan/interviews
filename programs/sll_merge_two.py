"""""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 

Input: list1 = 1 -> 2 -> 4, list2 = [1,3,4]
Output: [1,1,2,3,4,4]

a
1 -> 2 -> 4
b
None

head 1 -> 1
    			nn

"""
from single_linked_lists import Node

def merge_sll(a: Node, b: Node) -> Node : 
    head = Node(0)
    new_node = head
    while a != None and b != None :
        if a.data <= b.data :
            new_node.next = a 
            a = a.next
        else :
            new_node.next = b 
            b = b.next
        new_node = new_node.next
    if a == None :
        a = b
    while a != None :
        new_node.next = a 
        a = a.next
        new_node = new_node.next
    return head.next

a = Node.list_builder()
print(a)
b = Node.list_builder()
print(b)

print(merge_sll(a, b))
        

