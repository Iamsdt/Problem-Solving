class BTNode(object):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if data < self.data:
            # left node
            if self.left:
                pass
            else:
                self.left = BTNode(data)

        else:
            # right node
            if self.right:
                pass
            else:
                self.right = BTNode(data)
