# type: ignore
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = 0    

        for n in nums:
            answer ^= n

        for n in range(len(nums) + 1):
            answer ^= n

        return answer
