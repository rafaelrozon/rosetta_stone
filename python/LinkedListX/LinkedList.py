from .Node import Node
import Exception

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    def increase_size(self):
        self.length += 1

    def decrease_size(self):
        self.length -= 1

    def add_to_head(self, value):
        if self.is_empty():
            self.head = Node(value, None)
        else:
            self.head = Node(value, self.head)
        self.increase_size()

    def add_to_tail(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = Node(value, None)

        self.increase_size()

    def find_by_value(self, value):
        current = self.head

        while current.value != value:
            current = current.next

        if current == self.head and current.value != value
            return None

        return current

    def delete_by_value(self, value):
        if self.is_empty():
            raise Exception("List is empty")


