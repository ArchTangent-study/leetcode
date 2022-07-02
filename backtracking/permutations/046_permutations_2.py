from typing import List
from math import factorial

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Dynamic Programming Approach. Start from bottom and work up."""
        # NOTE: need to start with empty permutation for this to work
        answer = [[]]
        to_add = []

        # Refer to previous permuations from answer[0, end_ix] to make new ones
        for i, number in enumerate(nums):
            # Refer to previous permutations as a slice
            previous = answer[0: factorial(i)]
            for prev_permutation in previous:
                # Insert number at each index, using a *copy*
                for index in range(i+1):
                    permutation = prev_permutation[:]
                    permutation.insert(index, number)
                    to_add.append(permutation)
            # Remove previous permutations and add new ones
            answer.clear()
            answer.extend(to_add)
            to_add.clear()

        return answer
