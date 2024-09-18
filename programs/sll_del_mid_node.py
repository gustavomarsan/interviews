from single_linked_lists import Node

def del_mid_node(a, n) :
	found = False
	head = a
	if head.data == n :
		print("First element can´t be deleted")
		return head
	while a.next :
		if a.next.data == n and a.next.next :
			found = True
			a.next = a.next.next
			break
		if a.next.data == n and not a.next.next :
			found = True
			print("Last element can´t be deleted")
		a = a.next
	if found == False :
		print("The number wasn´t found ")
	return head
        	
a = Node.list_builder()
print(a)            
b = del_mid_node(a,int(input("What element you want to delete? ")))
print(b)
            