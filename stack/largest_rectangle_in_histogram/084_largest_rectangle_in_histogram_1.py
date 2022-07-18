from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Monotonic Stack. Add all values >= top of stack."""
        # stack holds index of height in heights
        highest = 0
        stack = []

        rightmost_ix = 0
        for incoming_ix, incoming_ht in enumerate(heights):
            rightmost_ix = incoming_ix
            # If incoming ht < top-of-stack ht, unwind and calculate area
            while stack and incoming_ht < heights[stack[-1]]:
                # Index and height of current (popped) bar
                ix = stack.pop()
                height = heights[ix]

                width = rightmost_ix - (stack[-1] + 1 if stack else 0)
                area = width * height
                if area > highest:
                    highest = area
                    
            # Add index of incoming bar to stack
            stack.append(incoming_ix)

        # End of iteration - handle all items left on stack
        rightmost_ix = len(heights)
        while stack:
            ix = stack.pop()
            height = heights[ix]

            width = rightmost_ix - (stack[-1] + 1 if stack else 0)
            area = width * height
            if area > highest:
                highest = area

        return highest
    