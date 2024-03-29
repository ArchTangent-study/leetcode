class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Divide and Conquer Approach w/Recursion"""
        if x == 0:
            return 0.0

        # Extract absolute value and sign of exponent
        exponent = abs(n)
        negative = n < 0

        def powHelper(power: int) -> float:
            # Base Cases
            if power == 0:
                return 1.0
            if power == 1:
                return x        

            # Divide the exponent in two
            new_n = power // 2
            rem_n = power % 2

            # Subproblems for exponent and any odd remainder
            subanswer = powHelper(new_n)
            remainder = x if rem_n == 1 else 1
            return subanswer * subanswer * remainder

        answer = powHelper(exponent)

        # Handle negative exponents at the end
        return 1 / answer if negative else answer
    