from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Pre-allocate to size n+1, since size is always known
        answer = [0]*(n + 1)
        
        for number in range(n + 1):
            # Bit count equals that of number >> 1, plus sign bit
            bit_count = answer[number >> 1] + number % 2
            # Number is the same as index in answer
            answer[number] = bit_count
            
        return answer
    