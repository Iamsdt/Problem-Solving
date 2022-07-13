import this


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.insert_helper(key, self.root)

    def insert_helper(self, key, node):
        if node.key > key:
            if not node.left:
                node.left = Node(key)
            else:
                self.insert_helper(key, node.left)
        else:
            if not node.right:
                node.right = Node(key)
            else:
                self.insert_helper(key, node.right)

    def in_order_successor(self, node):
        val = node

        while val.left:
            val = val.left
        
        return val

    def delete(self, node, key):
        if not node:
            raise Exception("Empty tree")

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # case 1: no child or single child
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif node.right:
                temp = node.left
                node = None
                return temp
            # case 2: multiple children
            temp = self.in_order_successor(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        return node
