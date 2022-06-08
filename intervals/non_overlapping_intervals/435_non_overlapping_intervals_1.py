from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by (start, end)          
        intervals.sort()
        # Running end value, initialized to minimum value in constraints
        running_end = -50000
        answer = 0
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            # Overlap - delete the interval w/highest end; keep one w/lowest
            if start < running_end:
                answer += 1
                running_end = min(end, running_end)
            else:
                # No overlap - update running endpoint
                running_end = end

        return answer
