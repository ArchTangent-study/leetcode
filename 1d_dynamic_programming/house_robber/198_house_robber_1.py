from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Gather highest of (a) current + 3 back, (b) current + 2 back or (b) 1 back
        # Start with house at index 2, using dummy value for 3 houses back
        house_ix = 2
        one_back = nums[1]
        two_back = nums[0]
        three_back = 0  
        highest = 0
        
        while house_ix < len(nums):
            # Money in current house
            current = nums[house_ix]
            # Highest value so far: 1 back, current + 2 back, or current + 3 back
            highest = max(one_back, two_back + current, three_back + current)
            # Move to next house, advancing three-house "window" by one step
            one_back, two_back, three_back = highest, one_back, two_back
            house_ix += 1

        # Return the highest running total
        return highest
