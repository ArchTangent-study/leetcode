from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Iterative DP approach.  Merge w/all others in list, then self.
    
        Each candidate is subject to two types of passes:
        1. Inclusive pass: the candidate is counted *1 or more times*
        (`starting_count = 1`). In other words, this pass must include 
        the candidate *t least once*.
        2. Optional pass:: the candidate is counted *0 or more times*
        (`starting_count = 0`), since all candidates after inclusive candidate 
        are optional.

        This ensures each possible combination is explored only once.
        """
        # Store all possible combinations
        answer = []
        i = 0

        def combo(
            i: int, starting_count: int, target: int, 
            running_sum: int, subset: List, candidates: List[int]
        ):
            # Early exit if out of bounds
            if not i < len(candidates):
                return
            # Candidate and max number of times it can be called
            c = candidates[i]
            max_count = target // c
            for count in range(starting_count, max_count+1):
                # Multiply candidate by current count and try:
                # - by itself
                # - with previous and next numbers
                number = c * count + running_sum
                if number == target:
                    # Multiples of candidate -> subset -> answer (e.g. [1,2,2,2])
                    # Optional (recursive) pass
                    new_subset = subset + [c] * count
                    answer.append(new_subset)
                elif number < target:
                    # Under target - pass this subset remaining numbers, counting from 0
                    # New running sum is the current number
                    # Optional (recursive) pass
                    new_subset = subset + [c] * count
                    combo(i+1, 0, target, number, new_subset, candidates)
                else:
                    # Overshot the target - no need to continue on this path
                    return

        # Inclusive Pass
        for i in range(len(candidates)):
            combo(i, 1, target, 0, [], candidates)

        return answer
