from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for subarray in matrix:
            # Is target bounded by subarray (min at [0]; max at [-1])?
            if target < subarray[0] or target > subarray[-1]:
                continue
            else:
                # If it is, return whether target is in the subarray
                return target in subarray            
            
        # Target wasn't in any subarray
        return False
        