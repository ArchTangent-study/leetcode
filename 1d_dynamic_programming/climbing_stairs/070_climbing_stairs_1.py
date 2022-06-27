class Solution:
    def climbStairs(self, n: int) -> int:
        # Uses an expanding list cache.
        ways = [0,1,2]

        if n < 3:
            return ways[n]

        answer = 0
        step = 3
        while step < n+1:
            # Each way is the answer from 1 step and 2 steps back, combined
            answer = ways[step-1] + ways[step-2]
            # Update the array of ways
            ways.append(answer)
            step += 1
    
        return answer
