from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Sliding window w/Deque. New highs replace all other values in queue."""
        # Early exit for length 1
        if k == 1: return [n for n in nums]

        answer = []
        queue = deque()         
        p1, p2 = 0, k-1
        last_ix = len(nums)

        # Build initial deque up to the (p2 - 1)th index
        # - add incoming and replace all others in front of it if higher
        for i, n in enumerate(nums[:p2]):
            while queue and n >= queue[-1][0]:
                queue.pop()
            queue.append((n, i))

        # Slide window, updating queue and answer.
        # - remove outgoing
        # - add incoming and replace all others in front of it if higher
        while p2 < last_ix:
            if queue[0][1] < p1:
                queue.popleft()

            incoming = nums[p2]

            while queue and incoming >= queue[-1][0]:
                queue.pop()
            queue.append((incoming, p2))

            answer.append(queue[0][0])

            p1 += 1
            p2 += 1

        return answer
