from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Min heap with absolute distance (no sqrt required)."""
        answer = []
        heap = []
        for x,y in points:
            abs_dist = x*x + y*y
            heapq.heappush(heap, [abs_dist, x, y])

        for _ in range(k):
            _,x,y = heapq.heappop(heap)
            answer.append([x,y])

        return answer