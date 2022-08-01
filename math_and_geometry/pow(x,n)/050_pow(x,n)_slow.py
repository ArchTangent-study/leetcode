# NOTE: this failed on TLE for x=0.00001, n=2147483647
# - issue: calls owHelper twice instead of storing result of one call and squaring it

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

            return powHelper(new_n) * powHelper(new_n) * powHelper(rem_n)

        answer = powHelper(exponent)

        # Handle negative exponents at the end
        return 1 / answer if negative else answer
    