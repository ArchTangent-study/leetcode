from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Key Ideas:
        - Gather consecutive high for each value and its L/R (-1, +1) neighbors
        - Assign consecutive lows for each value that is assigned a new high:
            - 'the high of X is Y.  The low of Y is X's low.'
        - Iterate over low map and take the highest `num->low` contiguous span        
        """
        # Store highest span so far
        answer = 0
        # Maps of {int: contiguous_high)} and {int: contiguous_low)} data
        high_map = {}
        low_map = {}
        for number in nums:
            # Update number and extant adjacent numbers with low.highest contiguous
            if number not in high_map:
                # lowest/highest contiguous value connected to this number
                low = low_map.get(number - 1,  number)
                high = high_map.get(number + 1,  number)
                # Update:
                # 1.) Current number with w/new low and high
                # 2.) Low number with w/new high
                # 3.) High number with w/new low
                high_map[number] = high
                high_map[low] = high
                low_map[number] = low                
                low_map[high] = low
                # Update highest span
                span = (high - low) + 1
                answer = max(answer, span)

        return answer
    