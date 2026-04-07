class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class MyStack:
    def __init__(self) -> None:
        self.head = None

    def push(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int:
        data = self.head.data
        self.head = self.head.next
        return data

    def top(self) -> int:
        return self.head.data

    def empty(self) -> bool:
        return self.head is None

class MyQueue:
    def __init__(self) -> None:
        self.stack_in = MyStack()
        self.stack_out = MyStack()

    def push(self, value) -> None:
        self.stack_in.push(value)

    def pop(self) -> int:
        self._get_stack_out()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._get_stack_out()
        return self.stack_out.top()

    def empty(self) -> bool:
        return self.stack_in.empty() and self.stack_out.empty()
    
    def _get_stack_out(self) -> None:
        if self.stack_out.empty():
            while not self.stack_in.empty():
                value = self.stack_in.pop()
                self.stack_out.push(value)
