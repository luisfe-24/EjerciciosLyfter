class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None


class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self, node):
        self.head = node
        self.tail = node

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, node):
        node.next = self.head
        self.head = node

    def push_right(self, node):
        self.tail.next = node
        self.tail = node

    def pop_left(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def pop_right(self):
        current_node = self.head
        while current_node.next is not self.tail:
            current_node = current_node.next

        current_node.next = None
        self.tail = current_node


first_node = Node("Medio (Inicial)")
deque = DoubleEndedQueue(first_node)

print("Estado inicial")
deque.print_structure()

deque.push_right(Node("Derecha 1"))
deque.push_left(Node("Izquierda 1"))

print("\n Push a los dos lados")
deque.print_structure()

deque.pop_left()
print("\nPop izq")
deque.print_structure()

deque.pop_right()
print("\nPop derecha")
deque.print_structure()

print("\nNuevo izq")
deque.push_left(Node("Izquierda 2"))

deque.print_structure()

print("\nPop derecho")

deque.pop_right()
deque.print_structure()
