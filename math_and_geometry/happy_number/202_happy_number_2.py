# type: ignore
class Solution:
    def isHappy(self, n: int) -> bool:
        # Store set of used numbers to check for repeats.
        repeat_numbers = set()
        
        while n != 1:
            n = self.sumOfSquares(n)
            if n in repeat_numbers:
                return False
            repeat_numbers.add(n)
            
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
    