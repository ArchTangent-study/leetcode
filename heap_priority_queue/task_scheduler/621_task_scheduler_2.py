from typing import List
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Heap and Queue. Of all tasks that are ready, choose one w/highest count."""
        timer = 0
        counter = {}      # task: count

        for task in tasks:
            if task in counter:
                counter[task] += 1
            else:
                counter[task] = 1

        # Heap of all ready tasks.  Sort by highest count
        ready = []
        for task, count in counter.items():
            heapq.heappush(ready, (-count, task))
        # Queue of tasks on cooldown.  Pulled from left; added to right
        waiting = deque()

        while ready or waiting:
            # Add to ready when timer > ready turn
            while waiting and timer > waiting[0][0]:
                _ready_turn, task = waiting.popleft()
                heapq.heappush(ready, (-counter[task], task))

            if ready:
                _, task = heapq.heappop(ready)  # gather task
                counter[task] -= 1

                # If task remains, add to waitlist with its ready turn
                if counter[task] > 0:
                    waiting.append((timer + n, task))

            # Pass one unit of time to (a) execute a task or (b) idle
            timer += 1

        return timer
