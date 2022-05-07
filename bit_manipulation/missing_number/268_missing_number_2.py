# type: ignore
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        expected = 0

        for n in nums:
            if n == expected:
                expected += 1
            else:
                return expected

        return expected    
