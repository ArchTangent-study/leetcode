# type: ignore
# Simple Solution using sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Use sorting to determine if list contains a duplicate."""
        nums.sort()

        previous = None
        for current in nums:
            if current == previous:
                return True
            previous = current

        return False
