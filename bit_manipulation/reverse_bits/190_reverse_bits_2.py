# type: ignore
class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        
        # Gather bits from right of n, assign to left of output
        for i in range(32):
            ith_bit = n >> i & 1
            output |= ith_bit << (31 - i)
            
        return output
