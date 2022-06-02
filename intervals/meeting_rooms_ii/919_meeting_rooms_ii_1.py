# type: ignore

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Unpack intervals into (time, is_start) pairs, sorted by time.
        # Start values increment the count, while end values decrement it.
        times = []
        for interval in intervals:
            times.append((interval.start, True))
            times.append((interval.end, False))
        times.sort()

        count = 0
        max_count = 0

        # Time is just used for sorting
        for (_time, is_start) in times:
            if is_start:
                count += 1
            else:
                # Only need to set max_count when a meeting ends
                max_count = max(count, max_count)
                count -= 1

        return max_count
