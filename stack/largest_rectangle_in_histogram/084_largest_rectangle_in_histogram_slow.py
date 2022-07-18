# Fails on Time Limit Exceeded, but is accurate. Time complexity: O(n^2)
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """More concise naive approach."""
        n = len(heights)
        highest = 0

        for i in range(0, n):
            for j in range(i + 1, n):
                # Widest rectangle from current index i to j
                temp = min(heights[i:j])
                if (j - i) * temp > highest:
                    highest = (j - i) * temp
            # Widest rectangle confined to right of this bar
            temp = min(heights[i:])
            if (n - i) * temp > highest:
                highest = (n - i) * temp

        return highest
