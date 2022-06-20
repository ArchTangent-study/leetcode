from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Key Idea: identify non-contiguous values in L->R direction."""
        # Store highest span so far
        answer = 0
        # Gather all numbers in a set to deduplicate
        number_set = {n for n in nums}
        # A number with nothing to its left is the start of a sequence
        for number in nums:
            if number - 1 in number_set:
                # Not a start of a sequence - pass to be consumed later
                continue
            else:
                # Start of sequence - count and remove all adjacent numbers to the right
                next = number + 1
                span = 1
                while next in number_set:
                    span += 1
                    number_set.remove(next)
                    next += 1
                # Update highest contiguous count
                answer = max(answer, span)

        return answer
