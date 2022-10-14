class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    '''
    nodes are linked. 
  
    list.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''

    def add(self, value):
        # here is two possibilities
        # if list is empty then add directly into head
        # or go to the last node and add
        node = Node(value)

        if self.head is None:
            self.head = node
            self.size += 1
            return

        # second possibilities
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        # now add
        temp.next = node
        self.size += 1

    def delete(self, value):
        if self.head is None:
            raise Exception("List is empty")

        # find node
        # node can be found on the top position
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return

        # now search
        # if node is on the middle position
        # 10 *11* 12
        # I want to remove node 11
        # so change the 10 next to 12
        # if node on the last
        # remove 12 then make 11 next node is null

        # Explanantion
        '''
        say we have 10 -> 11 -> 12 -> 13 -> None
        so, first temp will 10
        but we already check this value using if condition
        so we will compare temp.next (11)
        here our case we need to delete 12
        so, when temp value (11) and temp next (12) that is correct for delete node
        here we will change next value of temp (11)
        and temp next is the delete node
        so, update temp.next with delete node with next
        '''

        temp = self.head
        while temp.next is not None:
            if temp.next.value == value:
                deleteNode = temp.next
                temp.next = deleteNode.next
                self.size -= 1
                break

            temp = temp.next

    def search(self, value):
        if self.head is None:
            raise Exception("List is empty")

        node = None
        temp = self.head
        while temp is not None:
            if temp.value == value:
                node = temp
                break
            temp = temp.next

        return node

    '''
    Added any node to the top
    '''

    def add_top(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    '''
    Add node after any node
    '''

    def add_after(self, old_value, value):
        old = self.search(old_value)

        if old is None:
            raise Exception("Node not found")

        node = Node(value)
        node.next = old.next
        old.next = node
        self.size += 1

    '''
    print all the values
    '''

    def __str__(self):
        # show all the values
        values = []
        temp = self.head
        while temp is not None:
            values.append(temp.value)
            temp = temp.next

        # append none
        values.append("None")
        return f"{' -> '.join(str(v) for v in values)}"


# test
my_list = SingleLinkedList()
my_list.add(10)
my_list.add(11)
my_list.add(12)
my_list.add(13)
print(my_list)
# delete node
my_list.delete(12)
print(my_list)
# search node
print(my_list.search(12))
# add after
my_list.add_after(11, 14)
print(my_list)
