class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end="  ")
                if temp.next:
                    print("--->", end=" ")
                temp = temp.next
            print()
