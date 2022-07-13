class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if not self.head:
            self.head = Node(value)
            return

        # add end
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(value)

    def add_first(self, value):
        if not self.head:
            self.head = Node(value)
            return

        temp = self.head
        self.head = Node(value)
        self.head.next = temp

    def search(self, value):
        res = None
        temp = self.head
        while temp:
            if temp.value == value:
                res = temp
            temp = temp.next
        return res

    def remove(self, value):
        if not self.head:
            return -1

        if self.head.value == value:
            self.head = self.head.next
            return 1

        temp = self.head
        
        
        while temp.next:
            if temp.next.value == value:
                temp.next = temp.next.next
                return 1
            temp = temp.next

        return -1

    
    def read(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


if __name__ == '__main__':
    sl = SingleLinkedList()
    sl.add(1)
    sl.add(2)
    sl.add(3)
    sl.add_first(5)
    sl.add_first(6)
    
    sl.read()
    print("After remove")
    sl.remove(3)
    sl.read()
