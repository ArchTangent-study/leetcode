# type: ignore
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-weight for weight in stones]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # stone 1 has lower value, but more weight since negated
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
    
            child_stone = self.smashStones(s1, s2)
            
            if child_stone:
                heapq.heappush(stones, child_stone)
        
        # Must negate since we negated weights at start
        if len(stones) == 1:
            return -stones[0]
        
        # No stones remain
        return 0
        
        
    def smashStones(self, s1, s2) -> Optional[int]:
        # Larger stones are *more negative* in this version
        if s1 < s2:
            return s1 - s2

        # Stones are same weight -> return no stones
        return None
        