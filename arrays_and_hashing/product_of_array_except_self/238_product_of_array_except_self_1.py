from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Two-pass approach: product in L->R and then R->L directions."""
        # Forward pass: start with leftmost value set to 1
        fwd_product = nums[0]
        answer = [1]
        # Gather running L->R product from index[1] to end
        for n in nums[1:]:
            answer.append(fwd_product)
            fwd_product *= n     
        # Reverse pass: start from index[-2] (i, 2nd to last) and gather R->L product
        # from index[-1] (j, last index), moving to the left. Example:
        #   nums: [1, 2, 3, 4]
        #     ix:       [i  j]     i and j move left, j gathers leftward running product
        # answer: [1, 1, 2, 6]     from fwd pass
        # answer: [24,12,8, 6]     final answer, after rev pass
        rev_product = 1
        for i in range(len(nums) -2, -1, -1):
            j = i + 1
            rev_product *= nums[j]
            answer[i] *= rev_product
            i -= 1

        return answer
