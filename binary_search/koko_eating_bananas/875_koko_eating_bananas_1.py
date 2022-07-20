from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Binary Search with Minimization."""
        # Min and max amount of bananas to eat
        low_rate, high_rate = 1, max(piles)
        answer = 0

        while low_rate <= high_rate:
            # Max amount of bananas eaten per hour (k)
            eat_rate = (low_rate + high_rate) // 2
            # Hours to eat all piles
            hours_to_eat = sum(math.ceil(pile / eat_rate) for pile in piles)
            # If all bananas eaten in time, add result and look for slower eat rate
            if hours_to_eat <= h:
                answer = eat_rate
                high_rate = eat_rate - 1
            else:
                # Ate too slowly - eat faster by shifting lowest eat rate (L pointer)
                low_rate = eat_rate + 1

        return answer
