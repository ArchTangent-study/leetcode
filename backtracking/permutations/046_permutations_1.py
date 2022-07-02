from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Recursive Approach. All combinations that start w/each number."""
        answer = []

        def dfs(nums_so_far, remaining):
            """Depth-First Search. At end of string"""
            # Go over all remaining numbers and put them at head of line
            for new_number in remaining:
                new_nums_so_far = nums_so_far + [new_number]
                new_remaining = [n for n in remaining if n != new_number]
                # Call dfs on this new arrangement
                dfs(new_nums_so_far, new_remaining)
            # Base case - no remaining numbers - add permutation to answer
            if not remaining:
                answer.append(nums_so_far)
                return

        # DFS starting with every number in nums (e.g. [1,2,3,4])
        for number in nums:
            # This sequence starts with n
            nums_so_far = [number]
            remaining = [n for n in nums if n != number]
            dfs(nums_so_far, remaining)

        return answer
