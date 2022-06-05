# Search a 2D Matrix ([LC074](https://leetcode.com/problems/search-a-2d-matrix/))
Difficulty: **Medium**

## Problem

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10⁴ <= matrix[i][j], target <= 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- OOB errors when indexing (empty arrays)
- Very large matrices (not a problem as `m` and `n` are `<=100`)

## Procedure

### Method 1: Iterative Search

A simple approach using iteration.

Iterate over each subarray in the main array, and checks if the `target` is within the `min` (`subarray[0]`) and `max` (`subarray[-1]`) of the subarray.  If it is, iterate over the subarray and return `true` if target is found.  If it isn't, return `false`.

Thoughts:  while this way works and was quite fast (faster than **82.22%** of submissions), the problem specifies that the algorithm should be *efficient*.  There's likely a better way to do this (e.g. using *binary search*).

Time Complexity: `O(m + n)`

### Method 2: Double Binary Search

This builds upon the skills learned in the Binary Search [[LC704]](https://leetcode.com/problems/binary-search/) problem.

Steps:
1. Perform a binary search on the 1st-dimensional array, getting the `mid` subarray.
2. Check if the `target` is bound by the `min` (`subarray[0]`) and `max` (`subarray[-1]`) of the subarray.
3. If `target` is bound by the subarray, perform a binary search for `target` within the subarray.
    - if `target` is found by the binary search, return `true`
    - if `target` is *not* found, `false`
4. If `target` is bound by the subarray, continue top-level binary search in step `1`.
5. If all `target` is not bound by *any* of the subarrays, return `false`.

Pitfalls:
- Brackets when calculating middle indexes, e.g. `middle_ix = (left_ix + right_ix) // 2`
- Shifting left/right indexes *past* the middle index during binary search:
```python
if target < guess:
    right_ix = middle_ix - 1
```
- Returning `false` for both levels of the algorithm
    - when all subarrays are exhausted
    - when binary search in a subarray fails

Speed: this was almost **2x slower** than method 1, but due to use of binary search (`O(log(n))`), it might perform better on larger data sets.

## Results (Python 3)

**Method 1**: 48 ms, 14.5 MB (82.22%, 44.85%)

**Method 2**: 88 ms, 14.5 MB (10.92%, 8.18%)
