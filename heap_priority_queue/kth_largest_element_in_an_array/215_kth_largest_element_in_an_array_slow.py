# Fails on Time Limit Exceeded. Worst case: O(n²)
# Example: nums = [10,8,7,6,5,4,3,2,1,0,9,9,9,9,9,9,9,9,9,9] ; k = 10
# Can be made faster by:
# (1) inserting from top of queue when number is closer to highest in queue (queue[0])
# (2) inserting from bottom of queue when number is closer to lowest in queue (queue[-1])
from typing import List
from collections import deque

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Monotonically-decreasing stack as deque of length k."""
        queue = deque([nums[0]])

        # High side is left [0]; low side is right [-1]
        # 1st number already in deque
        for number in nums[1:]:
            if number >= queue[0]:
                queue.appendleft(number)
                if len(queue) > k:
                    queue.pop()
            elif number > queue[-1]:
                lowest = queue.pop()
                temp = deque()
                while number > queue[-1]:
                    temp.appendleft(queue.pop())
                
                queue.append(number)
                queue.extend(temp)
                
                if len(queue) < k:
                    queue.append(lowest)
                
            elif len(queue) < k:
                queue.append(number)

        # Get kth largest value at index [k-1]
        answer = queue[k-1]

        return answer
