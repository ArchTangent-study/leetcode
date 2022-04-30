# type: ignore
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 0:
            count += 1 & n
            n >>= 1
            
        # Once n is zero, we know there are no more `1`s present            
        return count
