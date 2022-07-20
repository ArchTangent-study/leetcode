from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Partitioned Binary Search w/Ascending Order Detection."""
        L, R = 0, len(nums) - 1
        answer = 5000   # max value as per constraints

        while L <= R:
            M = (L + R) // 2
            left_num = nums[L]
            middle_num = nums[M]
            right_num = nums[R]
            # If [L,M] is ascending, update answer and shift L. Else, do nothing
            if left_num <= middle_num:
                if left_num < answer:
                    answer = left_num
                L = M + 1            
            # If [M,R] is ascending, update answer and shift R. Else, do nothing
            if middle_num <= right_num:
                if middle_num < answer:
                    answer = middle_num
                R = M - 1

        return answer
