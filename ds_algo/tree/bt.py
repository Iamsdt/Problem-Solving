# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from audioop import add
from re import S


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = Node(data)

        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = Node(data)


    def in_order_traversal(self):
        elements = []
        # visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right sub tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        # add root
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        # add root
        elements.append(self.data)

        return elements

    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            return self.left and self.left.search(value)
        elif value > self.data:
            return self.right and self.right.search(value)

        return False



if __name__ == '__main__':
    numbers = [17, 4, 100, 52, 9, 18, 20, 100]
    tree = Node(numbers[0])
    for i in range(1, len(numbers)):
        tree.add_node(numbers[i])

    # print
    print(tree.in_order_traversal())
    print(tree.pre_order_traversal())
    print(tree.post_order_traversal())

    print(tree.search(100))