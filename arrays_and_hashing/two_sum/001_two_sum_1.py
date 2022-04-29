# type: ignore
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_f = len(nums)

        for (index_1, number_1) in enumerate(nums[0:index_f - 1]):
            index_2 = index_1 + 1
            for number_2 in nums[index_1+1:index_f]:
                if number_1 + number_2 == target:
                    return [index_1, index_2]
                else:
                    index_2 += 1

        # Should never see this as there is a guaranteed solution
        return [-1, -1]
