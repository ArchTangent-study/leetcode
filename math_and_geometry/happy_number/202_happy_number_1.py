# type: ignore
class Solution:
    def isHappy(self, n: int) -> bool:
        # Store set of known bad numbers from testing. Use only n < 10.
        bad_numbers = {2, 3, 4, 5, 6, 8, 9}
        
        while n != 1:
            n = self.sumOfSquares(n)
            if n in bad_numbers:
                return False
            
        return True
    
        
    def sumOfSquares(self, n: int) -> int:
        """Returns sum of squares for each *digit* in n."""
        answer = 0
        
        while n > 0:
            # Extract bottommost digit and shift n right by a decimal place
            digit = n % 10
            n //= 10
            answer += digit * digit
            
        return answer
    