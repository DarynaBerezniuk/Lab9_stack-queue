from collections import deque

class FreqStack:
    def __init__(self):
        self.freq_dict = {}
        self.stack_dict = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.freq_dict.get(val, 0) + 1
        self.freq_dict[val] = freq

        self.max_freq = max(self.max_freq, freq)

        if not freq in self.stack_dict:
            self.stack_dict[freq] = deque()

        self.stack_dict[freq].append(val)

    def pop(self) -> int:
        val = self.stack_dict[self.max_freq].pop()
        self.freq_dict[val] -= 1
    
        if not self.stack_dict[self.max_freq]:
            self.max_freq -= 1

        return val
