import heapq

class MedianFinder:

    def __init__(self):
        # One max heap (lower half) and one min heap (upper half)
        self.lower = []
        self.upper = []
        self.even = True

    def addNum(self, num: int) -> None:
        # Add numbers based on relation to upper/lower heaps
        # Adjust heaps based on length, always keeping them within 1
        # NOTE: since `lower` is a MAX heap, need to negate the number
        # NOTE: special case if both are empty
        len1, len2 = len(self.lower), len(self.upper)
        
        if len1 == 0 and len2 == 0:
            self.upper.append(num)
        elif num >= self.upper[0]:
            heapq.heappush(self.upper, num)
            len2 += 1
            if len2 - len1 > 1:
                moved_num = heapq.heappop(self.upper)
                heapq.heappush(self.lower, -moved_num)
        else:
            heapq.heappush(self.lower, -num)
            len1 += 1
            if len1 - len2 > 1:
                moved_num = heapq.heappop(self.lower)
                heapq.heappush(self.upper, -moved_num)

        # Toggle even/odd status
        if self.even:
            self.even = False
        else:
            self.even = True
            
        # print(f" lower: {self.lower}, upper: {self.upper}, even? {self.even}")

    def findMedian(self) -> float:
        # If even, take average of max_heap's high and min_heap's low
        # If odd, take the topmost value of the *larger* heap       
        # NOTE: need to negate the value of max heap (lower)
        
        # print(f"findMedian")
        # print(f" lower: {self.lower}, upper: {self.upper}, even? {self.even}")
        
        if self.even:
            return (-self.lower[0] + self.upper[0]) / 2
        else:
            return -self.lower[0] if len(self.lower) > len(self.upper) else self.upper[0]
