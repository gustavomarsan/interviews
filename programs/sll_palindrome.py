# check if a sll is a palindrome 
# it moves de sll to a list and then compare the list in a for comparing data from firs vs last 
# then firs +1 and  last -1 until get the center of the list


from single_linked_lists import Node

def palindrome(h: Node) -> bool :
    list = []
    while h :                                       # move the sll to a list
        list.append(h.data)
        h=h.next

    for first in range (0, len(list)//2):           # compare list fist vs last and walk
        last = (first+1) * -1
        if list[first] != list[last] :
            return False

    return True



h = Node.list_builder()
print(h)
print(palindrome(h))