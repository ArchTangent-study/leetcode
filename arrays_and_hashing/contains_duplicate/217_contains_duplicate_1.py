# type: ignore
# Simple Solution using Python stdlib's collections.defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)

        for num in nums:
            if counter[num] == 1:
                return True
            counter[num] += 1

        return False
