from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Non-overlapped intervals that are to left/right of newInterval
        left = []
        right = []

        for current in intervals:        
            # No overlap: current is left of newInterval: add to left list
            if current[1] < newInterval[0]:
                left.append(current)
            # No overlap: current is right of newInterval: add to right list
            elif current[0] > newInterval[1]:
                right.append(current)
            # Overlap occurs: expand newInterval to [min(starts), max(ends)]
            else:
                newInterval[0] = min(newInterval[0], current[0])
                newInterval[1] = max(newInterval[1], current[1])

        # Merge non-overlapping intervals with (possibly expanded) newInterval
        return left + [newInterval] + right
    