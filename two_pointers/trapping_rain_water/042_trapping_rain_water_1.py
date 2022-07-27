from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """Monotonically-decreasing stack."""
        # Stack of (ix, ht) pairs
        stack = []
        answer = 0

        # Compare each incoming (ix,ht) vs top of stack
        for ix, ht in enumerate(height):
            # Adjusted index for any incoming height that pops anothe from stack
            adj_ix = ix
            while stack and ht > stack[-1][1]:
                top_ix, top_ht = stack.pop()
                # Get water removed by popping top (ix, ht)
                # NOTE: only collect if there's enough height on left side to contain area
                if stack:
                    low_ht = min(ht, stack[0][1])
                    area = (low_ht - top_ht) * (adj_ix - top_ix)
                    answer += area
                    adj_ix = top_ix
                    
            stack.append((adj_ix, ht)) 

        return answer
