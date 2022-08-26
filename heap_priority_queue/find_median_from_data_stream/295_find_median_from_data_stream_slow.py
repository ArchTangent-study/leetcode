# This works, but fails on Time Limit Exceeded
import heapq

class MedianFinder:

    def __init__(self):
        self.nums = []
        self.even = True

    def addNum(self, num: int) -> None:
        heapq.heappush(self.nums, num)
        if self.even:
            self.even = False
        else:
            self.even = True

    def findMedian(self) -> float:
        # Store numbers to be re-added
        temp = []
        answer = 0

        # If even, add the first (len/2 + 1) values to temp and average top 2
        # If odd, add the first (len/2 + 1) values to temp and return top value
        # Afterwards, return temp values back to the heap
        for _ in range(len(self.nums) // 2 + 1):
            temp.append(heapq.heappop(self.nums))
  
        if self.even:
            answer = (temp[-1] + temp[-2]) / 2
        else:
            answer = temp[-1]

        for num in temp:
            heapq.heappush(self.nums, num)

        return answer