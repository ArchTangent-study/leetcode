from heapq import heappop, heappush
from typing import List, Tuple

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Sliding window w/max heap of (-val, ix) pairs."""
        answer = []
        p1, p2 = 0, k - 1       # set to k-1 for proper indexing

        # Build initial window of (-n, val) pairs
        # NOTE: Python's heap is min heap, so need to negate all values for max
        # NOTE: Start with window 1 left of bounds (from indexes -1 to k-2)
        heap = []
        for i, n in enumerate(nums[:p2]):
            heappush(heap, (-n, i))

        # Perform the following in order:
        # - Get incoming value from right of window (p2), add (-value, p2) to heap
        # - Get highest IN WINDOW value (ix >= p1) from heap and add to answer
        # - Slide window right by advancing p1 and p2
        while p2 < len(nums):

            incoming = nums[p2]
            heappush(heap, (-incoming, p2))

            # Check if top of heap is in window. If not, pop. If so, get its value
            while heap[0][1] < p1:
                heappop(heap)

            # Highest value is negative of value of the min heap
            highest = -heap[0][0]
            answer.append(highest)

            # Advance window
            p1 += 1
            p2 += 1

        return answer
    