from typing import List

class DetectSquares:
    """Improved version with (x,y) counter."""

    def __init__(self):
        # Dict of x:[y1, y2, ...] values
        self.x_to_y =  {}
        # Counter of specific (x,y) points
        # - saves time by tracking count directly: O(1) vs O(n)
        self.counter = {}

    def add(self, point: List[int]) -> None:
        """Adds y for given x, and x for given y."""
        x,y = point[0], point[1]
        
        if x in self.x_to_y:
            self.x_to_y[x].append(y)
        else:
            self.x_to_y[x] = [y]
            
        if (x,y) in self.counter:
            self.counter[(x,y)] += 1
        else:
            self.counter[(x,y)] = 1
        

    def count(self, point: List[int]) -> int:
        """Count possible squares by matching equidistant coaxial values."""
        answer = 0
        x,y = point[0], point[1]

        # Find other values with same x (coaxial) and get distance between them
        for y2 in self.x_to_y.get(x, []):
            dist = abs(y - y2)

            # Skip values that would have zero area
            if dist == 0:
                continue
            
            # Two possible squares that can be formed from two coaxial points
            # - positive x (x + distance, y) and (x + distance, y2)
            # - negative x (x - distance, y) and (x - distance, y2)
            pos1 = (x + dist, y)
            pos2 = (x + dist, y2)
            neg1 = (x - dist, y)
            neg2 = (x - dist, y2)
            
            # Count number of times each pair is found
            # Number of ways is each count multiplied by other
            pos_count = self.counter.get(pos1, 0) * self.counter.get(pos2, 0)
            answer += pos_count
            neg_count = self.counter.get(neg1, 0) * self.counter.get(neg2, 0)
            answer += neg_count     
          
        return answer
