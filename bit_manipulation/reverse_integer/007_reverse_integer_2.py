class Solution:
    def reverse(self, x: int) -> int:
        """Digit extraction and reversal with Overflow Margin."""
        # Use absolute value and sign to help w/Python's division on (-) numbers
        if x < 0:
            margin    = 2147483648   # abs(-2 ** 31)
            margin_10 =  214748364   # abs(-2 ** 31) // 10
            sign = -1
        elif x > 0:
            margin    = 2147483647    # 2 ** 31 - 1
            margin_10 =  214748364    # 2 ** 31 - 1 // 10
            sign = 1
        else:
            return 0                  # no digits to reverse

        number = abs(x) 
        answer = 0

        while number != 0:
            digit = number % 10
            
            # Overflow check: see if *shifting* running answer by 10 exceeds margin
            if margin_10 < answer:
                return 0   
            
            # Shift answer to left by one digit
            answer *= 10
            
            # Overflow check: see if *adding* to running answer by 10 exceeds margin
            if margin - answer < digit:
                return 0
            
            # Insert digit at rightmost spot (LSD)
            answer += digit

            number //= 10

        # Account for sign
        return answer * sign
