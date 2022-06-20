# NOTE: this works, but fails on time
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Map of {int: contiguous_high)} data
        map = {}
        for number in nums:
            # Update number and extant adjacent numbers with highest contiguous
            if number not in map:
                # highest contiguous value connected to this number
                high = number
                # if Right number is present, update high
                right_number = number + 1
                if right_number in map:
                    high = right_number
                # if Left number is present, update its contiguous high
                left_number = number - 1
                if left_number in map:
                    map[left_number] = high
                # Update current number
                map[number] = high

        # Iterate over map, moving from high to high and tracking highest range
        # NOTE: this part makes it O(n^2)
        answer = 0
        for number, high in map.items():
            n, h = number, high
            while h > n:
                n, h = h, map[h]
            answer = max(answer, h - number + 1)

        return answer
