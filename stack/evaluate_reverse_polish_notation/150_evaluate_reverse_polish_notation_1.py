from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Stack approach.  Each operator acts on two operands."""
        stack = []

        for token in tokens:
            # NOTE: watch the order! 1st item popped is the 2nd operand!
            # NOTE: Python requires int(op1 / op2) for division toward 0 for negatives!
            match token:
                case "+":
                    op2, op1 = stack.pop(), stack.pop()  
                    stack.append(op1 + op2)
                case "-":
                    op2, op1 = stack.pop(), stack.pop()  
                    stack.append(op1 - op2)
                case "*":
                    op2, op1 = stack.pop(), stack.pop()
                    stack.append(op1 * op2)
                case "/":
                    op2, op1 = stack.pop(), stack.pop()  
                    stack.append(int(op1 / op2))
                case _:
                    stack.append(int(token))

        # Answer is the number remaining in stack/register.
        return stack[0]
