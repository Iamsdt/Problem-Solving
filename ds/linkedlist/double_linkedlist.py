class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


'''
Available methods
1. add
2. add_last
3. search
4. add_after
5. delete
6. display_nodes
'''


class MyDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        node = Node(value)
        node.next = self.head

        if self.head is not None:
            self.head.prev = node

        self.head = node
        self.size += 1

    def add_last(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.size += 1
            return

        # go to the last position
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        # here temp node.next is null
        temp.next = node
        node.prev = temp
        self.size += 1

    def search(self, value):
        if self.head is None:
            raise Exception("List is empty")

        temp = self.head
        while temp is not None:
            if temp.value == value:
                break
            temp = temp.next

        return temp

    def add_after(self, prev_value, value):
        # search after node
        prev_node = self.search(prev_value)
        if prev_node is None:
            print("Previous node not found")
            return

        node = Node(value)

        # insert
        node.next = prev_node.next
        prev_node.next = node

        # set previous value
        node.prev = prev_node
        if node.next is not None:
            node.next.prev = node

        self.size += 1

    def delete(self, value):
        if self.head is None:
            raise Exception("List is empty")

        # check delete node is head or not
        if self.head.value == value:
            if self.head.next is not None:
                next_node = self.head.next
                next_node.prev = None
                self.head = next_node

            else:
                self.head = None

            self.size -= 1
            return

        delete_node = self.search(value)
        if delete_node is None:
            print("Delete node not found")
            return

        # take prev and next reference
        prev_node = delete_node.prev
        next_node = delete_node.next

        # now modify nodes
        if prev_node is not None:
            prev_node.next = next_node

        if next_node is not None:
            next_node.prev = prev_node

        self.size -= 1

    def display_nodes(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

        print("Total size: ", str(self.size))


dl = MyDoubleLinkedList()
dl.add(2)
dl.add(5)
dl.add(10)
dl.add_last(15)
dl.add_last(17)
dl.add_after(15, 16)
dl.add_after(10, 11)
dl.delete(10)
dl.display_nodes()


#docker run -it --device /dev/kvm -p 50922:10022 -v /tmp/.X11-unix:/tmp/.X11-unix -e "DISPLAY=${DISPLAY:-:0.0}" -e GENERATE_UNIQUE=true -e MASTER_PLIST_URL='https://raw.githubusercontent.com/sickcodes/osx-serial-generator/master/config-custom.plist' sickcodes/docker-osx:monterey