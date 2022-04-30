# type: ignore
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Principle: num ^ 0 = num; num ^ num = 0"""
        value = 0
               
        for number in nums:
            value = number ^ value
               
        return value
        