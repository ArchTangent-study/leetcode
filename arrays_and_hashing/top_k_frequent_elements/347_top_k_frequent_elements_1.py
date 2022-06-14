from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counts occurrence of each number. A defaultdict(int) would also work.
        counter = {}
        
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        # Collect all (number, count) pairs, sort by highest count
        counts = sorted(
            [(num, count) for num, count in counter.items()], 
            key=lambda i: i[1],
            reverse=True
        )

        # Return numbers with k highest count
        return [num for (num, _count) in counts[:k]]
    