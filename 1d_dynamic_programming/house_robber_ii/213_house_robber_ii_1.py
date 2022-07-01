from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """Two-pass DP approach. Max space between robbed houses: 2."""
        num_houses = len(nums)
        # Early exit
        if num_houses == 1:
            return nums[0]
        if num_houses == 2:
            return max(nums[0], nums[1])

        # Used for looping
        last_house_ix = num_houses - 1

        # 1st pass: include 1st house, *ignore last house*
        # Iterate starting from house at index 0, up to (not including) last house
        three_back, two_back, one_back = 0, 0, 0
        house_ix = 0
        pass_1_highest = 0
        while house_ix < last_house_ix: # ignore last house
            current = nums[house_ix]
            # Highest of one house back, or current plus two or three houses back
            pass_1_highest = max(one_back, two_back + current, three_back + current)
            # Move to next house, updating previous house with highest value
            one_back, two_back, three_back = pass_1_highest, one_back, three_back
            house_ix += 1

        # 2nd pass: ignore 1st house, allow last.
        # Iterate starting from house at index 1, up to (and including) last house
        three_back, two_back, one_back = 0, 0, 0
        house_ix = 1
        pass_2_highest = 0
        while house_ix <= last_house_ix: # include last house
            current = nums[house_ix]
            # Highest of one house back, or current plus two or three houses back
            pass_2_highest = max(one_back, two_back + current, three_back + current)
            # Move to next house, updating previous house with highest value
            one_back, two_back, three_back = pass_2_highest, one_back, three_back
            house_ix += 1

        # Compare pass that allows last house vs one that disallows it
        return max(pass_1_highest, pass_2_highest)
