# Find Minimum in Rotated Sorted Array ([LC153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/))
Difficulty: **Medium**

## Problem

Suppose an array of length n sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` `1` time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n)` time.

Constraints:
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Finding answer with `O(log n)` time complexity

## Procedure

### Method 1: Paritioned Binary Search w/Ascending Order Detection

Key Idea: the minimum of *any* ascending slice is the *first element*.

Big Picture:
1. `L, M, R = left, middle, right` pointers
2. Set default `answer = 5000`, the highest value as per constraints
3. Perform below steps while `L <= R`:
4. Check values at `[L,M]` for ascending order
    - if not ascending order, do nothing
    - if in ascending order:
        - update `answer` with minimum of itself or left value (`nums[L]`)
        - shift `L` to `M + 1`
5. Check values at `[M,R]` for ascending order
    - if not ascending order, do nothing
    - if in ascending order:
        - update `answer` with minimum of itself or middle value (`nums[M]`)
        - shift `R` to `M - 1`
6. return `answer`

Complexity:
- Time: split the problem space in half each time -> `O(log n)`
- Space: constant extra space required -> `O(1)`

## Results (Python 3)

**Method 1**: 38 ms, 14.2 MB (**97.56%**, 23.33%)
