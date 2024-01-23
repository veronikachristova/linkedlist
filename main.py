class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def vloz(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def zobraz(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.vloz(1)
linked_list.vloz(2)
linked_list.vloz(3)

linked_list.zobraz()
