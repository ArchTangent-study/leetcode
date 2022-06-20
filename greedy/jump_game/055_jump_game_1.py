from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Work backwards, incrementing minimum jump length needed to reach exit
        # Start with length of 0, as you need 0 to get to exit from exit
        jump_length_required = 0
        for n in nums[-1::-1]:
            # If current space lacks sufficient jump, add 1 for next space
            if n < jump_length_required:
                jump_length_required += 1
            else:
                # Reset minimum jump required to 1 for next tile
                jump_length_required = 1

        # If start is reached with a required jump > 1, fail.
        return jump_length_required == 1
    