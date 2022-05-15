from typing import List, Tuple

class MinStack:

    def __init__(self):
        # 2-tuple of (val, min_val) data
        self.stack: List[Tuple[int, int]] = []
        # max value as per constraints
        self.min_val = 2**31 -1
        
    def push(self, val: int) -> None:
        if val <= self.min_val:
            self.stack.append((val, val))
            self.min_val = val
        else:
            self.stack.append((val, self.min_val))

    def pop(self) -> None:
        self.stack.pop()
        # Need to update min_val to reflect possible changes
        if len(self.stack) > 0:
            self.min_val = self.stack[-1][1]
        else:
            # Reset min_val on empty stack to constraint maximum
            self.min_val = 2**31 - 1
    
    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.min_val
