# Median of Two Sorted Arrays ([LC004](https://leetcode.com/problems/median-of-two-sorted-arrays/))
Difficulty: **Hard**

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

Constraints:
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10⁶ <= nums1[i], nums2[i] <= 10⁶`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- `nums1` or `nums2` empty
- In which direction should the binary search be adjusted?
- Mismatched list sizes
- Negative numbers

## Procedure

### Method 1: Binary Search using Partition Width

Key Idea: adjust the number of values used in the shorter of the two lists until both lists have an *equal* number of values on the *left* of the combined list as the *right*.

Big Picture:
1. Set shortest list to be `ListA`, longest list to be `ListB`
2. Adjust number of left-side values from `ListA` (`M1`) using binary search
3. Number of left-side values from `ListB` (`M2`) is `combined_length // 2 - M1`
4. Slice `ListA` and `ListB` into left/right partitions based on lengths calculated
    - `LeftA`, `LeftB`, `RightA`, `RightB`
5. if `max(LeftA, LeftB)` < `min(RightA, RightB)`:
    - return the median based on `even/odd` `combined_length`
6. if highest value of `LeftA` > `min(RightA, RightB)`:
    - too many values in `LeftA` -> adjust `M1` downward
7. if highest value of `LeftB > min(RightA, RightB)`:
    - too many values in `LeftB` -> adjust `M1` upward (thereby `M2` downward)
8. If both partitions are empty, return `0.0`

Complexity:
- Time: `O(log m+n)`
- Space: constant extra space -> `O(1)`

## Results (Python 3)

**Method 1**: 144 ms, 14.2 MB (52.61 %, 68.31%)
