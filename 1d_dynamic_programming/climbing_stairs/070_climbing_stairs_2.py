class Solution:
    def climbStairs(self, n: int) -> int:
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
    