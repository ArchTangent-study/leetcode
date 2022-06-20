from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Forward attempt: keep moving as long as you have enough jump power
        jump_power = 0
        # Don't include final index because jump not needed once end reached
        for n in nums[:-1]:
            jump_power = max(jump_power, n)
            # You have enough jump - spend 1 jump power to move ahead
            if jump_power > 0:
                jump_power -= 1
            else:
                # Can't make the jump -> return False 
                return False

        # Made it to end without failing
        return True
