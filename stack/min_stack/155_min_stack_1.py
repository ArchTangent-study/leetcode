from typing import List, Tuple

class MinStack:

    def __init__(self):
        # 2-tuple of (val, min_val) data
        self.stack: List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or val <= self.stack[-1][1]:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][1]))
                   
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
