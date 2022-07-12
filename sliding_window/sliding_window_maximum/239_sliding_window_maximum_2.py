from heapq import heappop, heappush
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Sliding window w/max heap of (-val, ix) pairs.  Improved"""
        answer = []
        p1, p2 = 0, k - 1       # set to k-1 for proper indexing

        # Build initial window of (-n, val) pairs
        # NOTE: if incoming value is higher, clear all other values in heap
        heap = []
        for i, n in enumerate(nums[:p2]):
            heappush(heap, (-n, i))
            if -n <= heap[0][0]:
                heap[:] = [(-n, i)]

        # Perform the following in order:
        # - Add incoming (-value, p2) to heap
        # - Get highest IN WINDOW value (ix >= p1)
        # - If incoming is the highest, clear all values in heap except incoming
        # - Add highest heap value to answer
        # - Slide window right by advancing p1 and p2
        while p2 < len(nums):
            incoming = nums[p2]
            heappush(heap, (-incoming, p2))       

            while heap[0][1] < p1:
                heappop(heap)       
            highest = -heap[0][0]

            if -heap[0][0] == incoming:
                heap[:] = [(-incoming, p2)]

            answer.append(highest)

            p1 += 1
            p2 += 1

        return answer
    