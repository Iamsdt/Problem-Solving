class MyStack:
    def __init__(self):
        self.list = []
        self.head = 0
        self.size = 0

    '''
    stack is first come last out data structure
    so, when we pop we will get the data from head
    '''

    def pop(self):
        if self.head == -1:
            raise Exception("stack is empty")

        # reduce size
        self.size -= 1
        value = self.list[self.head]
        self.head -= 1

        return value

    '''
    When we push any value, we will save that value in the list
    using append and we will move header
    '''

    def push(self, value):
        self.list.append(value)
        self.head += 1
        self.size += 1

    def size(self):
        return self.size


# Now test
stack = MyStack()

stack.push(1)
stack.push(10)
stack.push(20)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.size)
