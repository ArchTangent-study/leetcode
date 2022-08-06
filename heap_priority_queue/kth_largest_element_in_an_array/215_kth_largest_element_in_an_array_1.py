from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """List-based Counter.  Takes advantage of -10000 to +10000 number range."""
        counter = [0] * 20001

        # Update count for each number. Note the indexing, where 0 is at index [10000]
        for number in nums:
            index = 10000 + number
            counter[index] += 1

        # Start from highest number, counting down until kth largest found
        k_remaining = k
        number = 10000
        for count in reversed(counter):
            if count >= k_remaining:
                return number
            k_remaining -= count
            number -= 1

        raise ValueError("Each input should have a valid solution!")\
