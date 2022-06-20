from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Key Idea: store current *lowest*/*highest* contiguous for each number."""
        # Store highest span so far
        answer = 0
        # Map of {int: (contiguous_low, contiguous_high)} data
        low_high_map = {}
        for number in nums:
            # Update number and extant adjacent numbers with low.highest contiguous
            if number not in low_high_map:
                # lowest/highest contiguous value connected to this number
                low = low_high_map.get(number - 1,  (number, number))[0]
                high = low_high_map.get(number + 1,  (number, number))[1]
                # Update:
                # 1.) Current number with w/new low and high
                # 2.) Low number with w/new high
                # 3.) High number with w/new low
                low_high_map[number] = (low, high)
                low_high_map[low] = (low, high)
                low_high_map[high] = (low, high)
                # Update highest span
                span = (high - low) + 1
                answer = max(answer, span)

        return answer