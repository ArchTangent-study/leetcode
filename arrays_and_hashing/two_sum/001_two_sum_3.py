# type: ignore
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Track { target_num, target_index } target pairs
        sum_table = {}

        for (ix, num) in enumerate(nums):
            if num in sum_table:
                return [ix, sum_table[num]]
            # Insert number that will complete the sum: (target - num)
            sum_table[target - num] = ix
            
        raise ValueError("A valid solution must be present!")
