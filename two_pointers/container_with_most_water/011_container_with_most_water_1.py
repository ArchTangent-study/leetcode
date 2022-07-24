from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Two Pointer Closing Window w/alternation based on highest L/R value"""
        highest_area = 0
        L, R = 0, len(height) - 1

        # Start from extremes and shift the index that has the *lowest* height
        while L < R:
            left_ht = height[L]
            right_ht = height[R]

            area = min(left_ht, right_ht) * (R - L)
            if area > highest_area:
                highest_area = area

            if left_ht < right_ht:
                L += 1
            else:
                R -= 1

        return highest_area
    