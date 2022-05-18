from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Returns index of `target` in nums, if present. Else, -1"""
        left_ix = 0
        right_ix = len(nums) - 1
               
        # Keep guessing at midpoint until L != R index
        while left_ix <= right_ix:
            mid_ix = (left_ix + right_ix) // 2
            guess = nums[mid_ix]
            
            if target == guess:
                return mid_ix
            elif target < guess:
                right_ix = mid_ix - 1
            elif target > guess:
                left_ix = mid_ix + 1
        
        # All guesses exhausted - target is not present
        return -1
        