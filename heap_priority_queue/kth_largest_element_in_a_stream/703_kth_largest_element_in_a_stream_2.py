# type: ignore
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        
        # Convert nums into binary heap (Python default is min heap)
        heapq.heapify(self.heap)
        
        # Remove all but k highest values (popping removes *lowest* value)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
            

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        # Remove all but k highest values (popping removes *lowest* value)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # In min heap, lowest value is at index [0]
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
