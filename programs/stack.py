# Sort stack. Wirte a program to sort a stack such that the smallest items are on the top. Ypu can use an additional
# temporary stack, but you may not copy the elements into any other data structure (such as array) 
# The stack supports the following operations, push, pop, peek, and is_empty
# usin a sll as a stack
#   bottom -> top

from single_linked_lists import Node

def push(a : Node, item: int) -> None:      # always that make a push insert it in order
    if is_empty(a):                         # if sll is empty
        a.data = item
        return
    while a.next:                           # insert value before a smaller value. Not for the last node 
        if item > a.data :
            newnode = Node(a.data)
            a.data = item
            newnode.next = a.next
            a.next = newnode
            
            return
        a = a.next
    if item > a.data :                      # if you are in the last node of sll and item > a.data, switch smalles to the end
        a.next = Node(a.data)
        a.data = item
    else :
        a.next = Node(item)                 # else if item is smaller than the last in sll, only add to the end
    return 

def pop(a: Node) -> None:
    if is_empty(a) :
        print("The stack is empty")
        return
    while a.next :                          
        if a.next.next :                    # if is there next.next, walk one step
            a = a.next
        else :                              # if the next is the last node, eliminate it
            a.next = None
            return

    a.data = None                           # when the sll has only 1 node, eliminate it

def is_empty(a: Node) -> bool :    
    if a.data == None:
        return True

head = Node(None)
print(is_empty(head))
pop(head)
push(head, 4)
push(head, 7)
push(head, 1)
push(head, 8)
push(head, 5)
push(head, 2)
print(head)
pop(head)
pop(head)
push(head, 3)
print(head)
push(head, 9)
push(head, 11)
push(head, 12)
push(head, 10)
print(head)
for i in range(7) :
    pop(head)
print(head)

