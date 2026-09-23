class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    top: Node

    def __init__(self, top):
        self.top = top

    def print_structure(self):
        current_node = self.top

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push(self, node):
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            self.top = self.top.next


first_node = Node("Hola")
structure = Stack(first_node)

second_node = Node("Segundo")
structure.push(second_node)

third_node = Node("3")
structure.push(third_node)

structure.print_structure()

print("\nEliminar head\n")

structure.pop()

structure.print_structure()
