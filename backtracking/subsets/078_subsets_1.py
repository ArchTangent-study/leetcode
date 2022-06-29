from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Iterative approach."""
        # Account for empty member of power set
        answer = [[]]
        to_add = []

        for n in nums:
            # Subgroups are empty ([]), single value ([2]) or multiple ([1,2])
            for subgroup in answer:
                to_add.append([*subgroup, n])
            # Add newly-merged combinations to answer
            answer.extend(to_add)
            # Clear to_add for later use
            to_add.clear()

        return answer
