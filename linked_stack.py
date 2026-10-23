class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False  # No fixed capacity

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: stack is empty.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.top.value

    def display(self):
        current = self.top
        items = []
        while current:
            items.append(current.value)
            current = current.next
        print("Stack (top to bottom):", items)