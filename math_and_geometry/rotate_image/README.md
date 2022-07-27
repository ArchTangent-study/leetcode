# Rotate Image ([LC048](https://leetcode.com/problems/rotate-image/))
Difficulty: **Medium**

## Problem

You are given an `n x n` 2D matrix representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

Constraints:
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Even vs odd `m,n` values
- Rotating in place
- Avoiding making a separate **2D** matrix

Thoughts:
- Can use similar approach as when rotating a point around a pivot

## Procedure

### Method 1: Transpose List

*Note*: this answer is valid, since the specification are not to make a separate **2D** matrix.  This method only uses a **1D** list of values to apply.

Key Ideas:
- store a `list` of all transpositions to make, then apply them in order.
- rotating `90º` clockwise is `(row, col) -> (col, n-1-row)`

Complexity:
- Time: one pass to gather transpositions, another to apply them -> `O(2n)` -> `O(n)`
- Space: store `list` of all transpositions to make -> `O(n)`

Thoughts:
- this had better space performance than expected (75%), especially since a separate list was used.

## Results (Python 3)

**Method 1**: 47 ms, 13.8 MB (68.66%, 74.54%)

**Method 2**:   ms,  MB (%, %)
