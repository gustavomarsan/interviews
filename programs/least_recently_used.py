# Implement an LRU (Least Recently Used) Cache.


class Node:
    def __init__(self, site: str, next=None, prev=None) -> None:
        self.site = site
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.site) + " -> " + str(self.next)

    def new_site(site: str, n) -> None:
        new_site = Node(site)
        new_site.prev = n
        n.next = new_site
        n = n.next
        return n

    def prev_site(n) -> None:
        if n.prev.site:
            n = n.prev
        return n

    def next_site(n) -> None:
        if n.next:
            prev_site = n
            n = n.next
        return n


head = Node(None)
head.prev = None
n = head

n = Node.new_site("nba.com", n)
n = Node.new_site("nfl.com", n)
n = Node.new_site("nbc.com", n)
n = Node.new_site("cnn.com", n)

print(head.next)
print(n.site)

n = Node.prev_site(n)
n = Node.prev_site(n)

print(head.next)
print(n.site)

n = Node.new_site("fast.com", n)
n = Node.new_site("weatherchanel.com", n)
n = Node.new_site("mlb.com", n)

print(head.next)
print(n)

n = Node.prev_site(n)

print(head.next)
print(n.site)

n = Node.new_site("amazon.com", n)

n = Node.prev_site(n)
n = Node.prev_site(n)
n = Node.prev_site(n)
n = Node.prev_site(n)


print(head.next)
print(n.site)

n = Node.next_site(n)
n = Node.next_site(n)
n = Node.next_site(n)

print(head.next)
print(n.site)

n = Node.new_site("totalplay.com", n)
print(head.next)
print(n.site)
