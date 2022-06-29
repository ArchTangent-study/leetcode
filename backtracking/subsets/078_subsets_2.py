from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Recursive approach with Depth-First Search based on index."""
        answer = []

        # Two choices: merge the number at given index, or do nothing.
        def dfs(ix: int, subset: List):
            # At the end of the tree -> add this branch's subset to answer
            if ix == len(nums):
                answer.append(subset)
                return

            # Separate copy for the right branch
            left, right = subset, subset.copy()

            # Decision 1: merge number at index into left side
            number = nums[ix]
            left.append(number)
            dfs(ix+1, left)

            # Decision 2: do not merge number - call DFS w/no changes
            dfs(ix+1, right)    

        dfs(0, [])

        return answer
        