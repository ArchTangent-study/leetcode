# type: ignore
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Sort nums from highest to lowest
        self.nums = sorted(nums, reverse=True)
        self.k = k

        # Remove all but k highest values (popping removes *lowest* value)
        while len(self.nums) > self.k:
            self.nums.pop()
            

    def add(self, val: int) -> int:       
        if len(self.nums) < self.k or val >= self.nums[-1]:
            self.nums.append(val)
            self.nums.sort(reverse=True)
        if len (self.nums) > self.k:
            self.nums.pop()
                    
        # Lowest value is at index [-1]
        return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
