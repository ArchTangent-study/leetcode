# type: ignore
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            s1, s2 = stones.pop(), stones.pop()
            
            child_stone = self.smashStones(s1, s2)
                
            if child_stone:
                stones.append(child_stone)
                stones.sort()    
         
        if len(stones) == 1:
            return stones[0]
    
        # No stones remain
        return 0
                
            
    def smashStones(self, s1, s2) -> Optional[int]:
        """Smash two stones together, returning remaining stone weight, if any"""
        if s1 < s2:
            return s2 - s1
        if s1 > s2:
            return s1 - s2
        
        # Stones are same weight -> return no stones
        return None
        