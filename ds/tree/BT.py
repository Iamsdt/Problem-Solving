from re import S


class BTNode(object):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.data == data:
            return

        if data < self.data:
            # left node
            if self.left:
                self.left.add_node(data)
            else:
                self.left = BTNode(data)

        else:
            # right node
            if self.right:
                self.right.add_node(data)
            else:
                self.right = BTNode(data)

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

    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            # it's on the left tree
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            # this is the right tree
            if self.right:
                return self.right.search(value)
            else:
                return False

    def get_max(self):
        if self.right is None:
            return self.data
        
        return self.right.get_max()

    def get_min(self):
        if self.left is None:
            return self.data
        
        return self.left.get_min()

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.get_min()
            self.data = min_val
            self.right = self.right.delete(min_val)


def build_tree(elements):
    root = BTNode(elements[0])
    for i in range(1, len(elements)):
        root.add_node(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 100, 52, 9, 18, 20, 100, ]
    tree = build_tree(numbers)
    print(tree.in_order_traversal())
    print(tree.search(21))
    print("Maximum", tree.get_max())
    print("Minimum", tree.get_min())

    print("Delete")
    tree.delete(18)
    print(tree.in_order_traversal())
        


