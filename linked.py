class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, item):
        if self.head is None:
            self.head = Node(item)

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(item)