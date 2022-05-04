# type: ignore
class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
  
        # Integer size is 32: shift 32 times
        for i in range(32):
            lsb = n & 1
            
            # Must shift output before inserting LSB
            output <<= 1
            output |= lsb
            
            n >>= 1
            
        return output
