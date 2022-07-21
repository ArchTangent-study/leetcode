from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Two Pointer Closing Window."""
        L, R = 0, len(numbers) - 1

        while L < R:
            combined = numbers[L] + numbers[R]

            if combined == target:
                return [L+1, R+1]

            if combined > target:
                R -= 1
            else:
                L += 1

        raise ValueError("A single answer is guaranteed!")
