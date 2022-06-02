# type: ignore

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Unpack intervals into (time, counter_mod) pairs, sorted by time.
        # Start values increment the count, while end values decrement it.
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        times.sort()

        count = 0
        max_count = 0
        
        # Time is just used for sorting
        for (_time, counter_mod) in times:
            count += counter_mod
            max_count = max(count, max_count)

        return max_count
