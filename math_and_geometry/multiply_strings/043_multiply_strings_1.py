class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Digital Product Addition with Digit Shift."""
        digits = 0

        # Multiply each digit in num1 by those of num2, accounting for digit shift
        # Add each product to digits
        for ix1, d1 in enumerate(reversed(num1)):
            for ix2, d2 in enumerate(reversed(num2)):
                digit_shift = 10 ** (ix1 + ix2)
                product = int(d1) * int(d2) * digit_shift
                digits += product

        # Convert digits to string and return
        return str(digits)
        