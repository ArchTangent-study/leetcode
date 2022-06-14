from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Map count to numbers w/that count. A defaultdict(list) would also work.
        k_tracker = defaultdict(list)
        # Map numbers to their count. A defaultdict(int) would also work.
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
            new_count = counter[num]
            k_tracker[new_count].append(num)

        # Starting at highest count, work downward until k highest nums collected
        # Be sure to account for missing key and decrement highest_count
        # Set is needed to avoid duplicates in k_tracker
        highest_count = max(counter.values())
        top_k = set()

        while len(top_k) < k:
            if highest_count in k_tracker:
                top_k.update(k_tracker[highest_count])
            highest_count -= 1

        # Return numbers with k highest count
        return [*top_k]
