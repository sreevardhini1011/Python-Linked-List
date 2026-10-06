class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def put(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

        self.size += 1

    def remove(self):
        if self.top is None:
            raise IndexError("Stack is empty — nothing to pop out!")

        value = self.top.value
        self.top = self.top.next

        self.size -= 1

        return value

    def peek(self):
        if self.top is None:
            raise IndexError("Stack is empty!")

        return self.top.value

    def is_empty(self):
        return self.top is None

    