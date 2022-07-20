# Search in Rotated Sorted Array ([LC033](https://leetcode.com/problems/search-in-rotated-sorted-array/))
Difficulty: **Medium**

## Problem

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
- `1 <= nums.length <= 5000`
- `-10⁴ <= nums[i] <= 10⁴`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10⁴ <= target <= 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Performing in `O(log n)` time

## Procedure

### Method 1: Bifurcated Binary Search w/Ascension Detection

Key Ideas:
1. A possibly rotated sorted array will consist of `1` or `2` ascending regions
2. Once an ascending region is found, we can perform binary search within that region *if* the `target` is possibly contained in that region

Big Picture:
1. Establish `L,M,R = left, middle, right` pointers
2. Perform the below steps while `L <= R`
3. Check `[L,M]` for (a) ascending order and (b) target in bounds
    - if not ascending order, do nothing
    - if `target` not within `[L,M]`: shift `L` to `M+1`
    - if `target` within `[L,M]`: return `binarySearch()` with starting bounds of `[L,M]`
4. Check `[M,R]` for (a) ascending order and (b) target in bounds
    - if not ascending order, do nothing
    - if `target` not within `[M,R]`: shift `R` to `M-1`
    - if `target` within `[M,R]`: return `binarySearch()` with starting bounds of `[M,R]`
5. If answer not found, return `-1`

Complexity:
- Time: eliminate L/R regions, binary search in correct region -> `O(3 log n)` -> `O(log n)`
- Space: constant extra space -> `O(1)`  

## Results (Python 3)

**Method 1**: 66 ms, 14.2 MB (46.73 %, **90.91%**)
