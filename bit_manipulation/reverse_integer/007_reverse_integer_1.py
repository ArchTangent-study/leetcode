class Solution:
    def reverse(self, x: int) -> int:
        """Digit extraction and reversal."""
        MIN_VAL = -2147483649   # -2 ** 31 - 1
        MAX_VAL = 2147483648    # 2 ** 31
        # Helps with Python's way of dividing negative integers
        number = abs(x) 
        sign = -1 if x < 0 else 1
        digits = []

        while number != 0:
            digit = number % 10
            digits.append(digit)
            number //= 10

        answer = sum(10 ** i * d for i,d in enumerate(reversed(digits))) * sign

        if not (MIN_VAL < answer < MAX_VAL):
            return 0

        return answer        
        