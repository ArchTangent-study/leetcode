class Solution:
    def climbStairs(self, n: int) -> int:
        # The number of step combinations for `number` is equal to sum of those of
        # `number - 1` and `number - 2` combined.

        # Number of combinations for these is already known
        ways = {
            1: 1,
            2: 2,
        }
        
        if n in ways:
            return ways[n]
        
        # Increment n while summing each n-1, n-2
        for number in range(3, n + 1):
            ways[number] = ways[number-1] + ways[number-2]
            
        return ways[n]
    