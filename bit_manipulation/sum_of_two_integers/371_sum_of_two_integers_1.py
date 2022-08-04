class Solution:
    def getSum(self, a: int, b: int) -> int:
        """Bitwise Addition and Subtraction w/Carry and Bitmask"""

        def bitAdd(n1: int, n2: int) -> int: 
            """Iterate over bits (up to 10 with max number of 1,000) and add w/carry"""
            answer = 0
            carry = 0
            bitmask = 1
            high_mask = 1001
            # Two objectives:
            # - set answer bit according to n1/n2 bits and carry
            # - set carry for next bit
            while bitmask < high_mask or carry:
                bit1 = n1 & bitmask
                bit2 = n2 & bitmask

                answer |= bit1 ^ bit2 ^ carry
                carry = (bit1 & bit2 | bit1 & carry | bit2 & carry) << 1
                bitmask <<= 1

            return answer

        def bitSub(n1: int, n2: int) -> int: 
            """Subtract n2 from n1 (perform n1 - n2) w/bit iteration"""
            answer = 0
            carry = 0
            bitmask = 1
            high_mask = 1001
            # Two objectives:
            # - set answer bit according to n1/n2 bits and carry
            # - set carry for next bit
            while bitmask < high_mask or carry:
                bit1 = n1 & bitmask
                bit2 = n2 & bitmask
                
                answer |= bit1 ^ bit2 ^ carry
                if bit2 and not bit1:
                    carry = bitmask << 1
                else:
                    carry = 0
                bitmask <<= 1

            return answer

        if a == 0:
            return b
        elif b == 0:
            return a
        elif a > 0 and b > 0:
            # Two (+) numbers: add normally
            return bitAdd(a, b)
        elif a < 0 and b < 0:
            # Two (-) numbers: add, preserving (-) sign
            return -bitAdd(abs(a), abs(b))
        else:
            # One (-) number - subtract smaller from larger number
            # - then set sign based on magnitude of (-) WRT (+)
            n1, n2 = abs(a), abs(b)
            answer = bitSub(n1, n2) if n1 > n2 else bitSub(n2, n1)
            if (a < 0 and n1 > n2) or (b < 0 and n2 > n1):
                return -answer
            return answer 
