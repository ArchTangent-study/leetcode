# type: ignore

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings

    class Interval:
        start: int
        end: int
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by start position
        intervals.sort(key=lambda i: i.start)

        # Start at 2nd interval (at 1st index). 
        # If 0 or 1 intervals, automatically passed.
        for ix in range(1, len(intervals)):
            previous = intervals[ix - 1]
            current = intervals[ix]

            # If previous meeting ends after current one starts, fail.
            if previous.end > current.start:
                return False
                
        # If no meeting overlap, you can attend all meetings
        return True
