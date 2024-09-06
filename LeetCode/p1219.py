class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = node

    def delete(self, value):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.val == value:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.val == value:
                temp.next = temp.next.next
                return

            temp = temp.next

    def search(self, value):
        if self.head is None:
            raise Exception("List is empty")

        temp = self.head
        while temp:
            if temp.val == value:
                return temp.val
            temp = temp.next

    def __str__(self):
        # show all the values
        values = []
        temp = self.head
        while temp is not None:
            values.append(temp.val)
            temp = temp.next
        # append none
        values.append("None")
        return f"{' -> '.join(str(v) for v in values)}"


if __name__ == "__main__":
    linked_list = SingleLinkedList()
    # add operation
    linked_list.add(10)
    linked_list.add(20)
    print(linked_list)
    linked_list.delete(30)
    print(linked_list)
    print(linked_list.search(20))
