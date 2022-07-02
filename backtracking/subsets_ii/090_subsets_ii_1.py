from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Dynamic Programming using *count* of each number."""
        # Gather numbers by count - use set to deduplicate (can also use dict)
        numbers = {(n, nums.count(n)) for n in nums}
        # Empty subset is part of the power set
        answer = [[]]
        to_add = []
        # For copy of each subset in answer, insert number up to `count` times
        for number, count in numbers:
            for subset in answer:
                for c in range(count, 0, -1):
                    new_subset = subset + [number] * c
                    to_add.append(new_subset)
            answer.extend(to_add)
            to_add.clear()

        return answer
