from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        # Running merged interval equal to last interval seen or merged
        running = [intervals[0][0], intervals[0][1]]

        for current in intervals:
            # No overlap: add running interval to answer, then set it current
            if current[1] < running[0] or current[0] > running[1]:
                merged.append(running)
                running = current
            # Overlap: merge current into running interval and continue
            else:
                running[0] = min(running[0], current[0])
                running[1] = max(running[1], current[1])

        # Add the running merged interval to the final result and return
        merged.append(running)

        return merged
    