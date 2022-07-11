# Gets right answers, but failed on Time Limit Exceeded
# - failure case: nums = [*range(10^4, 10^-4, -1)], k = 10007
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Sliding window w/early exit."""
        if k == 1:
            return [n for n in nums]

        answer = []
        max_ix = -1             # ix of highest value *within the window*
        max_num = -10001        # 1 under lowest value per constraints
        p1, p2 = 0, k - 1       # set to k-1 for proper indexing

        # Build initial window, advance window, and lower index of maxmimum
        for i, val in enumerate(nums[p1:p2+1]):
            if val > max_num:
                max_num = val
                max_ix = i
        answer.append(max_num)
        max_ix -= 1
        p1 += 1
        p2 += 1

        # Slide window up to end, updating max number, index, and answer
        while p2 < len(nums):
            # Replace max if:
            # - incoming is higher
            # - current max leaves window: scan for new high
            incoming = nums[p2]
            if incoming > max_num:
                max_num = incoming
                max_ix = k - 1
            elif max_ix < 0:
                # Reset max num to 1 below lowest value of constraints
                max_num = -10001 
                for i, val in enumerate(nums[p1:p2+1]):
                    if val > max_num:
                        max_num = val
                        max_ix = i

            # Add current max to answer
            answer.append(max_num)

            # Advance window and decrment index of max value in window
            max_ix -= 1
            p1 += 1
            p2 += 1

        return answer
    