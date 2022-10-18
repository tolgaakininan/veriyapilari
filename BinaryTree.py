class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add(self, data):
        if self.data == None:
            self.data = data
        else:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add(data)

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.data)
        if self.right is not None:
            self.right.print_tree()


tree = Node(1)
tree.add(3)
tree.add(4)
tree.add(7)
tree.add(6)
tree.add(7)
tree.print_tree()
