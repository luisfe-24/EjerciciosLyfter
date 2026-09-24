class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head: Node

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while (current_node.next != None):
                current_node = current_node.next

            current_node.next = new_node

    def delete(self, data):
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        else:
            current_node = self.head
            while current_node.next != None:
                if current_node.next.data == data:
                    current_node.next = current_node.next.next
                    return

                current_node = current_node.next

    def print_all(self):
        result = ""
        current_node = self.head

        while (current_node != None):
            if result == "":
                result = str(current_node.data)
            else:
                result = result + " -> " + str(current_node.data)

            current_node = current_node.next

        print(result)


ll = LinkedList()

ll.insert_front(10)
ll.insert_front(20)

ll.print_all()

ll.insert_back(30)

ll.print_all()

ll.delete(10)

ll.print_all()
