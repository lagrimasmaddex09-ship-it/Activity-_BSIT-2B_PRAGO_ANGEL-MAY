class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False  # No fixed capacity

    def enqueue(self, value):
        node = Node(value)

        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node

        self.rear = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: queue is empty.")

        value = self.front.value
        self.front = self.front.next
        self.size -= 1

        if self.front is None:
            self.rear = None

        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.front.value

    def display(self):
        current = self.front
        items = []

        while current:
            items.append(current.value)
            current = current.next

        print("Queue (front to rear):", items)