class MyHashMap:

    def __init__(self):
        self.n = 5381
        self.table = [None] * self.n

    def put(self, key: int, value: int) -> None:
        i = key % self.n
        self.table[i] = Node(key, value, self.table[i])

    def get(self, key: int) -> int:
        i = key % self.n
        node = self.table[i]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        i = key % self.n
        node = self.table[i]
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
            else:
                node = node.next
                
        if self.table[i] and self.table[i].key == key:
            self.table[i] = self.table[i].next
                
        
class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next