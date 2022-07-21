from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Binary Search, summing numbers at indexes S and M."""
        # Starting pointer (index of 1st number in sum)
        S = 0
        n = len(numbers)

        # NOTE: S and L cannot start at same index (could result in S and M being same)
        while S < n:
            L, R = S + 1, n - 1        
            while L <= R:
                M = (L + R) // 2

                combined = numbers[S] + numbers[M]

                if combined == target:
                    return [S+1, M+1]

                if combined > target:
                    R = M - 1
                else:    
                    L = M + 1
                    
            # New starting value
            S += 1

        raise ValueError("A single answer is guaranteed!")
        