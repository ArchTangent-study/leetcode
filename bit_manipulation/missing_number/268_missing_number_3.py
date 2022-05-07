# type: ignore
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arithmetic_sum = n * (n + 1) // 2
        sum_of_list = sum(nums)

        return arithmetic_sum - sum_of_list
