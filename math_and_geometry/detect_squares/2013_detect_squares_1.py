from typing import List

class DetectSquares:

    def __init__(self):
        # Dict of x:[y1, y2, ...] values
        self.x_to_y =  {}      

    def add(self, point: List[int]) -> None:
        """Adds y for given x, and x for given y."""
        x,y = point[0], point[1]
        
        if x in self.x_to_y:
            self.x_to_y[x].append(y)
        else:
            self.x_to_y[x] = [y]

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
            pos_x = x + dist
            neg_x = x - dist
            
            # Count number of times each pair is found
            # Pair 1
            pos1_count = self.x_to_y.get(pos_x, []).count(y)
            pos2_count = self.x_to_y.get(pos_x, []).count(y2)
            # Number of ways is each count multiplied by other
            pos_count = pos1_count * pos2_count
            answer += pos_count
            
            # Pair 2
            neg1_count = self.x_to_y.get(neg_x, []).count(y)
            neg2_count = self.x_to_y.get(neg_x, []).count(y2)
            # Number of ways is each count multiplied by other
            neg_count = neg1_count * neg2_count
            answer += neg_count

        return answer
