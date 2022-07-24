from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Two Pointers w/Early Exit based on highest possible area."""
        highest_area = 0
        last_ix = len(height) - 1

        # From current container (left) side, calculate:
        # - Area from itself to farthest side
        # - Max possible area *not* including farthest side
        # If no area could possibly exceed current highest area, move to next side
        for L, left_ht in enumerate(height):
            R = last_ix

            while L < R:            
                right_ht = height[R]

                area = min(left_ht, right_ht) * (R - L)
                if area > highest_area:
                    highest_area = area

                # Check if area could possibly get higher than current.
                # - If so, bring R pointer inward and continue
                # - Otherwise, shift left pointer (continue enumeration)
                max_possible_area = left_ht * (R - L - 1)
                if max_possible_area > highest_area:
                    R -= 1
                else:
                    break

        return highest_area
