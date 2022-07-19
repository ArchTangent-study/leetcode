from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Two-pass monotonically-increasing (strict) stack using count*height.
        
        Count all bars >= current bar:
        - to bar's left
        - to bar's right
        Then include itself to calculate area:
        - area = (1 + left_count + right_count) * height
        """
        n = len(heights)
        highest = 0
        counts = [0] * n
        # Strict, monotonically-increasing stack of (index, count)
        # NOTE: any values left in stack are unused - no value to left/right
        stack = []
        # Left to Right pass        
        # If value on top of stack >= incoming value:
        # - increment count by difference in index (ix - stack ix) and pop stack
        # - *lower* the "effective index" of incoming by count
        for ix, height in enumerate(heights):
            count = 0
            while stack and stack[-1][1] >= height:
                count = ix - stack[-1][0]
                stack.pop()
            counts[ix] += count
            effective_ix = ix - count
            stack.append((effective_ix, height))

        # Right to Left pass
        # If value on top of stack >= incoming value:
        # - increment count by difference in index (stack ix - ix) and pop stack
        # - *raise* the "effective index" of incoming by count
        stack.clear()

        for ni, height in enumerate(heights[-1::-1], start=1):
            ix = n - ni
            count = 0
            while stack and stack[-1][1] >= height:
                count = stack[-1][0] - ix
                stack.pop()
            counts[ix] += count
            effective_ix = ix + count
            stack.append((effective_ix, height))

        # Area pass
        for ix, height in enumerate(heights):
            area = (1 + counts[ix]) * height
            if area > highest:
                highest = area

        return highest