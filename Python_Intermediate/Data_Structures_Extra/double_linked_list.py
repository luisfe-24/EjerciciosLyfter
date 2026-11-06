class Node:
    data: str
    next: "Node"
    prev: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head

            self.head = new_node

    def delete(self, data):
        current_node = self.head

        while current_node != None:
            if current_node.data == data:
                if current_node.prev == None and current_node.next == None:
                    self.head = None
                    self.tail = None
                elif current_node.prev == None:
                    self.head = current_node.next
                    current_node.next.prev = None
                elif current_node.next == None:
                    self.tail = current_node.prev
                    current_node.prev.next = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next

    def print_forward(self):
        result = ""
        current_node = self.head

        while (current_node != None):
            if result == "":
                result = str(current_node.data)
            else:
                result = result + " -> " + str(current_node.data)

            current_node = current_node.next

        print(result)

    def print_backward(self):
        result = ""
        current_node = self.tail

        while (current_node != None):
            if result == "":
                result = str(current_node.data)
            else:
                result = result + " -> " + str(current_node.data)

            current_node = current_node.prev

        print(result)


dll = DoubleLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")

dll.print_forward()
dll.print_backward()

dll.prepend("X")

dll.print_forward()
dll.print_backward()

dll.delete("B")

dll.print_forward()
dll.print_backward()
