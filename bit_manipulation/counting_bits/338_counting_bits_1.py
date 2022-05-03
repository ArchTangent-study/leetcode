# type: ignore
class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(0, n+1):
            count = 0
            # Inner copy of i for use in the loop
            inner_i = i  
            while inner_i != 0:
                count += inner_i & 1 
                inner_i >>= 1
                
            answer.append(count)
                    
        return answer
