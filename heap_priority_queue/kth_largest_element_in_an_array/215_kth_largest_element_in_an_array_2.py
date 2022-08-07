# Note: this fails on TLE due to worst-case O(n²) time complexity.  Average is O(n).
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Quickselect with half-length pivot (iterative)."""
        length = len(nums)

        # Invalid data
        if length == 0:
            raise ValueError("no numbers provided!")
        if k < 0 or k > length:
            raise ValueError("Must have 0 < k <= len(numbers)!")

        # Can loop forever since answer will be present
        while True:
            length = len(nums)

            # Base Cases: find largest or smallest number in list
            if k == 1:
                return max(nums)
            if k == length:
                return min(nums)

            # Iterative case: pivot and choose either left or right side
            # NOTE: pivot is added to the LHS, after everything less than it
            pivot_ix = length // 2
            pivot = nums[length // 2]

            right = []
       
            for n in nums[:pivot_ix]:
                if n >= pivot:
                    right.append(n)
            for n in nums[pivot_ix+1:]:
                if n >= pivot:
                    right.append(n)

            # Right side is valid        
            if len(right) >= k:
                nums = right
                continue
                
            # Left side is valid
            nums = [n for n in nums if n < pivot]
            nums.append(pivot)
            k = k - len(right)