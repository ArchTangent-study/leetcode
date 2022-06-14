from typing import List, Dict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Map count to numbers w/that count. A defaultdict(list) would also work.
        k_tracker: Dict[int, List] = {}
        # Map numbers to their count. A defaultdict(int) would also work.
        counter: Dict[int, int] = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
                new_count = counter[num]
                if new_count in k_tracker:
                    k_tracker[new_count].append(num)
                else:
                    k_tracker[new_count] = [num]
            else:
                counter[num] = 1
                if 1 in k_tracker:
                    k_tracker[1].append(num)
                else:
                    k_tracker[1] = [num]

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
    