class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, value: int) -> None:
        new_node = Node(value)
        if self.empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self) -> int:
        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return data

    def peek(self) -> int:
        return self.head.data

    def empty(self) -> bool:
        return self.head is None

class MyStack:
    def __init__(self) -> None:
        self.queue1 = MyQueue()
        self.queue2 = MyQueue()

    def push(self, value: int) -> None:
        self.queue2.push(value)

        while not self.queue1.empty():
            self.queue2.push(self.queue1.pop())

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.pop()

    def top(self) -> int:
        return self.queue1.peek()

    def empty(self) -> bool:
        return self.queue1.empty()
