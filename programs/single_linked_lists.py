class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data) + " -> " + str(self.next)

    @staticmethod
    def list_builder():
        nodes = int(input("How many nodes? "))
        head = Node(None)
        n = head
        for i in range(nodes):
            new_node = Node(int(input(f"Node {i} : ")))
            n.next = new_node
            n = n.next
        return head.next
