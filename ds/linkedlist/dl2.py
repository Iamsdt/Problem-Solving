class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None



class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if not self.head:
            self.head = Node(value)
            return


        temp = Node(value)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def read(self):
        temp = self.head
        while temp:
            print(temp.value, sep=",")
            temp = temp.next

    def remove(self, value):
        if not self.head:
            raise ValueError("Empty list")

        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
            return

        temp = self.head
        while temp:
            if temp.value == value:
                prev = temp.prev
                next = temp.next
                if prev:
                    prev.next = next

                if next:
                    next.prev = prev

            temp = temp.next




if __name__ == '__main__':
    sl = DoublyLinkedList()
    sl.add(1)
    sl.add(2)
    sl.add(3)
    sl.add(5)
    sl.add(6)
    sl.add(7)
    sl.add(8)
    
    # sl.add_first(5)
    # sl.add_first(6)
    
    sl.read()
    print("After remove")
    sl.remove(2)
    sl.read()