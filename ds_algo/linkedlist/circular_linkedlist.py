class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedlist:
    def __init__(self, value):
        self.head = None
        self.size = 0

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        temp = self.head

