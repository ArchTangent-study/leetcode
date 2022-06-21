from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        # Power of current jump and highest available reserve jump
        current_jump = 0
        reserve_jump = 0
        distance = len(nums) - 1
        for number in nums:
            reserve_jump = max(reserve_jump, number)
            # You can jump to the exit
            if current_jump >= distance:
                return jumps
            # You can jump to the exit using reserve jump
            if reserve_jump >= distance:
                return jumps + 1            
            # Current jump has ended. Reset to reserve, and increment jumps
            if current_jump == 0:
                current_jump = reserve_jump
                jumps += 1
            # Move to next index: lower jump power and distance
            reserve_jump -= 1
            current_jump -= 1
            distance -= 1

        raise ValueError("Contraints require a valid answer!")
