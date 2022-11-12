# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return 0

        node = TreeNode(value)

        temp = self.root
        while temp:
            if temp.value == value:
                return -1

            if value < temp.value:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = node
                    break
            elif value > temp.value:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = node
                    break

    def iot(self, node):
        res = []
        if node.left:
            res += self.iot(node.left)

        res.append(node.value)
        
        if node.right:
            res += self.iot(node.right)
        

        return res
                

    def in_order_traversal(self):
        res = []
        if not self.root:
            raise Exception("Empty Tree")

        res += self.iot(self.root.left)
        res.append(self.root.value)
        res += self.iot(self.root.right)

        return res

    def in_order_traversal(self):
        res = []
        if not self.root:
            raise Exception("Empty Tree")

        res += self.iot(self.root.left)
        res.append(self.root.value)
        res += self.iot(self.root.right)

        return res

    def pot(self, node):
        res = []
        res.append(node.value)

        if node.left:
            res += self.pot(node.left)
        
        if node.right:
            res += self.pot(node.right)
        
        return res

    def pre_order_traversal(self):
        res = []
        if not self.root:
            raise Exception("Empty Tree")

        res.append(self.root.value)
        res += self.pot(self.root.left)
        res += self.pot(self.root.right)

        return res

    def post(self, node):
        res = []

        if node.left:
            res += self.post(node.left)
        
        if node.right:
            res += self.post(node.right)

        res.append(node.value)
        
        return res


    def post_order_traversal(self):
        res = []
        if not self.root:
            raise Exception("Empty Tree")

        res += self.post(self.root.left)
        res += self.post(self.root.right)
        res.append(self.root.value)

        return res


#######################################
############## ALGO ###################
def depth_first_search(node):
    res = []
    stack = [node]
    while stack:
        cu =  stack.pop()
        res.append(cu.value)
        if cu.right:
            stack.append(cu.right)
        if cu.left:
            stack.append(cu.left)

    return res


def breadth_first_search(node):
    res = []
    queue = [node]
    while queue:
        cu =  queue.pop(0)
        res.append(cu.value)
        if cu.left:
            queue.append(cu.left)    
        if cu.right:
            queue.append(cu.right)

    return res

def tree_search(node, target):
    stack = [node]
    while stack:
        cu = stack.pop()
        if cu.value == target:
            return True
        # else check I have to go right or left
        if target < cu.value and cu.left:
            stack.append(cu.left)
        elif target > cu.value and cu.right:
            stack.append(cu.right)

    return False


def tree_search2(node, target):
    temp = node
    while temp:
        if temp.value == target:
            return True
        # else check I have to go right or left
        if target < temp.value:
            temp = temp.left
        elif target > temp.value:
            temp = temp.right

    return False

def total_sum(node):
    res = 0
    stack = [node]
    while stack:
        cu =  stack.pop()
        res += cu.value
        if cu.right:
            stack.append(cu.right)
        if cu.left:
            stack.append(cu.left)

    return res


def total_sum2(node):

    if not node:
        return 0

    res = 0

    if node.left:
        res += total_sum2(node.left)
    if node.right:
        res += total_sum2(node.right)

    res += node.value

    return res


def tree_min(node):
    res = -float('-inf')
    stack = [node]
    while stack:
        cu =  stack.pop()
        res = min(cu.value, res)
        if cu.right:
            stack.append(cu.right)
        if cu.left:
            stack.append(cu.left)

    return res


def tree_min2(node):
    # min value will be only left value
    res = -float('-inf')
    stack = [node]
    while stack:
        cu =  stack.pop()
        res = min(cu.value, res)
        if cu.left:
            stack.append(cu.left)

    return res


def tree_min3(node):
    # min value will be only left value
    res = -float('-inf')
    temp = node
    while temp:
        res = temp.value
        temp = temp.left

    return res

def tree_max(node):
    # min value will be only left value
    res = -float('-inf')
    temp = node
    while temp:
        res = temp.value
        temp = temp.right

    return res

def max_path_sum(node):
    if not node:
        return 0

    # for leaf node
    if (not node.left and not node.right):
        return node.value

    value = max(max_path_sum(node.left), max_path_sum(node.right))

    return node.value + value

    
        


if __name__ == "__main__":
    tree = Tree()
    ri = [11, 6, 9, 20, 4, 10, 5, 17, 42, 50, 30]
    for i in ri:
        tree.add(i)
    
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())

    # lets delete tree
    print(depth_first_search(tree.root))
    print(breadth_first_search(tree.root))
    print("\nTree search")
    print(tree_search(tree.root, 50))
    print(tree_search2(tree.root, 50))
    print("\nTotal Sum")
    print(total_sum(tree.root))
    print(total_sum2(tree.root))
    print("\nFind Tree min")
    print(tree_min(tree.root))
    print(tree_min2(tree.root))
    print(tree_min3(tree.root))
    print(tree_max(tree.root))

    print(max_path_sum(tree.root))
    

# need to learn
# binary search tree
# auto balance BST
# after delete, or insert it should balance

# Delete from the tree
