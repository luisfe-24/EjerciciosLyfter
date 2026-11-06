class Node:
    data: str
    left: "Node"
    right: "Node"

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root

    def print_tree(self, current_node):
        if current_node is None:
            return

        print(current_node.data)
        self.print_tree(current_node.left)
        self.print_tree(current_node.right)

    def print_structure(self):
        self.print_tree(self.root)


root_node = Node("A")
tree = BinaryTree(root_node)

tree.root.left = Node("B")
tree.root.left.left = Node("D")

tree.root.right = Node("C")

tree.print_structure()
