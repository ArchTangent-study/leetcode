from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Backwards iteration w/high tracking."""
        n = len(temperatures)
        answer = [0] * n

        # Lowest per constraints is 30
        highest = 29
        high_ix = -1

        # Start from back
        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            # New high
            if temp > highest:
                highest = temp
                high_ix = i
                answer[i] = 0
                continue
            # Search for higher day from next day (i+1) to highest day (high_ix)
            num_days = 1
            for j in range(i+1, high_ix+1):
                next_temp = temperatures[j]
                if next_temp > temp:
                    answer[i] = num_days
                    break
                num_days += 1

        return answer
        