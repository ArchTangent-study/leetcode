class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
               
        # Store combinations for 2 and 1
        answer = 0
        minus_1, minus_2 = 2, 1
        
        # Increment n while summing each n-1, n-2, starting at 3
        for _number in range(3, n+1):
            answer = minus_1 + minus_2
            minus_1, minus_2 = answer, minus_1
                               
        return answer
    