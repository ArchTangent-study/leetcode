from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search on 1st dimension (top-level, m)
        top_left_ix = 0
        top_right_ix = len(matrix) - 1
        
        while top_left_ix <= top_right_ix:
            top_middle_ix = (top_left_ix + top_right_ix) // 2
            subarray = matrix[top_middle_ix]

            # If target < lowest value in subarray, shift window to left
            if target < subarray[0]:
                top_right_ix = top_middle_ix - 1
                continue
            # If target > highest value in subarray, shift window to right
            if target > subarray[-1]:
                top_left_ix = top_middle_ix + 1
                continue                              
            # If target is bounded by this subarray, perform binary search
            left_ix = 0
            right_ix = len(subarray) - 1                     

            while left_ix <= right_ix:
                middle_ix = (left_ix + right_ix) // 2
                guess = subarray[middle_ix]

                if target == guess:
                    return True
                if target < guess:
                    right_ix = middle_ix - 1
                    continue
                if target > guess:
                    left_ix = middle_ix + 1
                    continue
            
            # Target wasn't in a bounded subarray
            return False
            
        # Target wasn't in any subarray
        return False
        