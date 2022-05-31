from typing import List, Tuple

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Divide and Conquer method.

        Key Ideas:
        - Three key parts: Left, Inner, Right
        - Inner is the running contiguous sum, connecting left-pivot-right
        - Left must be connected to the leftmost part of a node
        - Right must be connected to the rightmost part of a node
        - Highest: highest value (individual or otherwise) found so far
        """
        return max(contiguousSum(nums))


def contiguousSum(nums: List[int]) -> Tuple[int, int, int, int]:
    """Returns highest (left, inner, right, high) values for a given node."""
    length = len(nums)
    # 1st base case: len == 1
    if length == 1:
        lhs = inner = rhs = high = nums[0]
        return (lhs, inner, rhs, high)
    # 2nd base case: len == 2 
    if length == 2:
        left, right = (nums[0], nums[1])
        lhs = max(left, left + right)
        rhs = max(right, left + right)
        inner = left + right
        high = max(left, right)
        return (lhs, inner, rhs, high)
    # Recursive case: len > 2
    mid = length // 2
    pivot = nums[mid]
    lhs_l, lhs_i, lhs_r, lhs_h = contiguousSum(nums[:mid])
    rhs_l, rhs_i, rhs_r, rhs_h = contiguousSum(nums[mid + 1:])
    
    # Highest left-facing, (LHS), right-facing (RHS), and pivot-facing contiguous values
    lhs = max(lhs_l, lhs_i + pivot, lhs_i + pivot + rhs_l)
    rhs = max(rhs_r, rhs_i + pivot, rhs_i + pivot + lhs_r)
    # Running sum across LHS, pivot, and RHS
    inner = lhs_i + pivot + rhs_i
    # Establish current highest value from above
    high = max(
        lhs_h, pivot, rhs_h, lhs, rhs,
        lhs_r + pivot, pivot + rhs_l, lhs_r + pivot + rhs_l
    )

    return lhs, inner, rhs, high
