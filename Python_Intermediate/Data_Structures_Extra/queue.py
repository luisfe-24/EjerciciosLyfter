class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    head: Node

    def __init__(self):
        self.head = None

    def print_all(self):
        result = ""
        current_node = self.head

        while (current_node is not None):
            if result == "":
                result = current_node.data
            else:
                result = result + " -> " + current_node.data

            current_node = current_node.next

        print(result)

    def enqueue(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node

        else:
            current_node = self.head
            while (current_node.next != None):
                current_node = current_node.next

            current_node.next = new_node

    def dequeue(self):
        if self.head == None:
            return None

        removed_data = self.head.data
        self.head = self.head.next
        return f'"{removed_data}"'


q = Queue()

q.enqueue("A")
q.enqueue("B")

q.print_all()

print(q.dequeue())
