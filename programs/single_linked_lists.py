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

    def list_builder(self):
        for i in range(int(input("How many nodes? "))):
            nn = Node(int(input(f"Node {i} : ")))
            if i == 0:
                n = nn
                h = n
                h.head = n
            n.next = nn
            n = n.next
        return h
