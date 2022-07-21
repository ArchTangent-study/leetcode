from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Two Pointer approach w/early exit."""
        L = 0
        n = len(numbers)

        while L < n:
            R = L + 1
            
            while R < n:
                combined = numbers[L] + numbers[R]
                
                if combined == target:
                    return[L+1, R+1]
                
                if combined > target:
                    break
                    
                R += 1
            L += 1

        raise ValueError("A single answer is guaranteed!")