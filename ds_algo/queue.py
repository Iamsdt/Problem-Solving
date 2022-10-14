class MyQueue:
    def __init__(self):
        self.list = []
        self.head = 0
        self.tail = 0

    '''
    queue is first come first out data structure
    so, when we dequeue we will get the data from head
    '''

    def dequeue(self):
        if self.head == self.tail:
            print("Queue is empty")
            return

        # reduce size
        value = self.list[self.head]
        self.head += 1

        return value

    def enqueue(self, value):
        self.list.append(value)
        self.tail += 1


# Now test
queue = MyQueue()

queue.enqueue(1)
queue.enqueue(10)
queue.enqueue(20)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
