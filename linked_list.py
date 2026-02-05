class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

node4.prev = node3
node3.prev = node2
node2.prev = node1

head = node1
tail = node4

current = head

while current:
    print(current.data, end = "=>")
    current = current.next

print(None)