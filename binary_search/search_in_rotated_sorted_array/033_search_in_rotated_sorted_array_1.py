from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Bifurcated Binary Search.  Check (a) ascending order (b) target presence."""
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
   
            middle_num = nums[middle]
            if middle_num == target:
                return middle
            
            # Check Left -> Middle for (a) ascending order and (b) target presence
            # If not ascending, do nothing
            left_num = nums[left]
            if left_num <= middle_num:
                # Target is bounded by [Left,Middle]. Do binary search
                if left_num <= target <= middle_num:
                    return binSearch(nums, target, left, right)
                else:
                    # Ascending but target not bounded. Shift left pointer past middle
                    left = middle + 1
                    
            # Check Middle -> Right (a) ascending order and (b) target presence
            # If not ascending, do nothing
            right_num = nums[right]
            if right_num >= middle_num:
                # Target is bounded by [Middle,Right]. Do binary search
                if middle_num <= target <= right_num:
                    return binSearch(nums, target, left, right)
                else:
                    # Ascending but target not bounded. Shift right pointer past middle
                    right = middle - 1

        # Number wasn't found in any bounds
        return -1        

def binSearch(nums, target, left_start, right_start):
    """Binary search helper function.  Preserves indices."""
    left, right = left_start, right_start
    
    while left <= right:
        middle = (left + right) // 2
        guess = nums[middle]
        if target == guess:
            return middle
        elif target > guess:
            left = middle + 1
        else:
            right = middle - 1

    return -1
