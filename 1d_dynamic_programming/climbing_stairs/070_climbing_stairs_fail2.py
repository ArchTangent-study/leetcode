class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursive method fails .  Early exit for base cases.
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
