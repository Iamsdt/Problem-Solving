class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class CircularLinkedlist:
    def __init__(self):
        self.last = None
        self.size = 0

    def add(self, value):
        if self.last is None:
            self.last = Node(value)
            return

        # if head null
        if not self.last.next:
            self.last.next = Node(value)
            return

        temp = self.last.next

        while temp and temp.next and temp.next != self.last:
            temp = temp.next

        if not temp:
            temp = Node(value, self.last)
        else:
            temp.next = Node(value, self.last)

        self.size += 1

    def add_top(self, value):
        if self.last is None:
            self.last = Node(value)
            return

        # if head null
        if not self.last.next:
            self.last.next = Node(value)
            return

        temp = self.last.next
        self.last.next = Node(value, temp)
        self.size += 1

    def delete(self, value):
        if not self.last:
            raise Exception("Empty List")

        temp = self.last.next
        if temp.value == value:
            self.last.next = self.last.next.next
            return 1

        while temp.next and temp != self.last:
            if temp.next.value == value and temp.next == self.last:
                temp.next = temp.next.next
                self.last = temp
                return 1
            elif temp.next.value == value:
                temp.next = temp.next.next
                return 1
            temp = temp.next

        return 0

    def traverse(self):
        res = []

        if not self.last:
            return res

        res.append(self.last.value)

        temp = self.last.next
        while temp and temp != self.last:
            res.append(temp.value)
            temp = temp.next
        # now add last
        return res


if __name__ == "__main__":
    li = CircularLinkedlist()
    li.add(10)
    li.add(15)
    li.add(20)
    li.add(30)
    li.add_top(50)
    # li.add(50)
    li.add(60)
    print(li.traverse())
    li.delete(10)
    print(li.traverse())
    li.delete(60)
    print(li.traverse())
