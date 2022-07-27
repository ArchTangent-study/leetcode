from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """Two Pointers with Highest Left/Right Value."""
        answer = 0
        highest = 0
        highest_left = []

        for ht in height:
            highest_left.append(highest)
            if ht > highest:
                highest = ht

        ix = len(height) - 1
        highest_right = 0

        for ht in reversed(height):
            # Get area over this particular index/slice
            effective_ht = min(highest_left[ix], highest_right)
            area = effective_ht - ht

            if area > 0:
                answer += area

            if ht > highest_right:
                highest_right = ht

            ix -= 1

        return answer
