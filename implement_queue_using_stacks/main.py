class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class MyQueue:

    def __init__(self):
        self.stack_in = None
        self.stack_out = None
        
    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.stack_in
        self.stack_in = new_node
        
    def pop(self) -> int:
        self._get_out_stack()

        data = self.stack_out.data
        self.stack_out = self.stack_out.next
        return data

    def peek(self) -> int:
        self._get_out_stack()

        return self.stack_out.data
        
    def empty(self) -> bool:
        return not self.stack_out and not self.stack_in
        
    def _get_out_stack(self) -> None:
        if not self.stack_out:
            while self.stack_in:
                temp = self.stack_in
                self.stack_in = self.stack_in.next

                temp.next = self.stack_out
                self.stack_out = temp



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
