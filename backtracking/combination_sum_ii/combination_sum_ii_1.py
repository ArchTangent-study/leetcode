from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """Dynamic Programming w/Deduplication and Counting."""
        answer = []
        # Count & deduplicate all candidates -> { c: count }
        numbers = {}
        for c in candidates:
            if c in numbers:
                numbers[c] += 1
            else:
                numbers[c] = 1
        # Combinations that are less than target.  Needs empty list to work
        combos = [[]]
        to_add = []
        # Extend each combination in combos with candidate, then add candidate by itself
        for number, count in numbers.items():
            # NOTE: ensures multiple starts at 1
            for multiple in range(1, count+1):
                product = number * multiple
                if product > target:
                    continue
                for combo in combos:
                    new_sum = sum(combo) + product
                    if new_sum > target:
                        continue
                    elif new_sum == target:
                        # Found a match - add directly to answer
                        # NOTE: this adds a copy
                        answer.append(combo + [number] * multiple)
                    else:
                        # New combination < target - store for later candidate
                        # NOTE: this adds a copy
                        to_add.append(combo + [number] * multiple)        
            # Move newly-made combinations to combo list
            combos.extend(to_add)
            to_add.clear()

        return answer 
