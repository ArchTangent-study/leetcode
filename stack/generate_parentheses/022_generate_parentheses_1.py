from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Backtracking: generate all combinations of open indexes and close w/stack"""
        answer = []

        def backtrack(open_n, closing_n, current):
            """Recursively build parentheses from `current` state."""
            # Base case: finshed buidling all parens
            if open_n == closing_n == n:
                answer.append(current)
                return
            # Left path: add open parens if more are needed
            if open_n < n:
                backtrack(open_n + 1, closing_n, current + "(")
            # Right path: add closing parens only if fewer than open
            if closing_n < open_n:
                backtrack(open_n, closing_n + 1, current + ")")

        # Start with opening parens, since all valid parens start w/open
        backtrack(1, 0, "(")

        return answer
