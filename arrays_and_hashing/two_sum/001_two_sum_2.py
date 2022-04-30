# type: ignore
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sort list low to high
        sorted_numbers = sorted(nums)
        range_1_f = len(sorted_numbers) - 1
        range_2_f = len(sorted_numbers)

        for (index_1, number_1) in enumerate(sorted_numbers[0:range_1_f]):
            # No valid sum if (lowest val + highest val) is < target
            if number_1 + sorted_numbers[-1] < target:
                continue

            for number_2 in sorted_numbers[index_1 + 1:range_2_f]:
                if number_1 + number_2 == target:
                    # Get index from left AND right side to avoid duplicate indexes
                    return [nums.index(number_1), self.rindex_list(nums, number_2)]
                
        # Error condition - shouldn't see as this as there is a guaranteed solution
        return [-1, -1]
        
    def rindex_list(self, li, x):
        """Python's rindex(), but for lists."""
        for i in reversed(range(len(li))):
            if li[i] == x:
                return i

        raise ValueError("{} is not in list".format(x))
