from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Reverse Iteration Dynamic Programming"""
        n = len(temperatures)
        answer = [0] * n
        # Start from back
        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            # Check if tomorrow is higher. If not, use DP to check future days
            next_ix = i+1
            while next_ix < n:
                future_temp = temperatures[next_ix]
                if future_temp > temp:
                    day_shift = next_ix - i
                    answer[i] = day_shift
                    break
                # Check a future day by using the previously-stored answer
                # NOTE: if answer at this spot is 0, it's the highest so far -> stop
                if answer[next_ix] == 0:
                    break
                next_ix = next_ix + answer[next_ix]

        return answer
    