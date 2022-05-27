from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Case where len == 1
        if len(nums) == 1:
            return nums[0]

        # Set to minimum possible integer
        highest_sum = -sys.maxsize - 1
        running_sum = -sys.maxsize - 1

        # Case where len == 2 (window of [num: running_sum])
        for num in nums:        
            running_sum = max(num, num + running_sum)
            if running_sum > highest_sum:
                highest_sum = running_sum
        
        return highest_sum
                        