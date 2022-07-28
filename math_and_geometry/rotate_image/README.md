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
- Even vs odd `n` values
- Rotating in place
- Avoiding making a separate **2D** matrix

Thoughts:
- Can use similar approach as when rotating a point around a pivot

Notes:
- Apparently, **reverse and transpose** is highly-effective method to solve this.

## Procedure

### Method 1: Transpose List

*Note*: this answer is valid, since the specification are not to make a separate **2D** matrix.  This method only uses a **1D** list of values to apply.

Key Ideas:
- store a `list` of all transpositions to make, then apply them in order.
- rotating `90º` clockwise is `(row, col) -> (col, n-1-row)`

Complexity:
- Time: one pass to gather transpositions, another to apply them -> `O(2n)` -> `O(n)`
- Space: store `list` of all transpositions to make -> `O(n)`

Where `n` is the width and `height` of the `matrix`

Thoughts:
- this had better space performance than expected (75%), especially since a separate list was used.

### Method 2: Outside-in Ring Rotation w/Tuple Unpacking

Key Idea: for a matrix of width `n`, rotate the first `n-1` values of the outer "ring" in groups of `4` using tuple unpacking

Complexity:
- Time: `O(n²)`
- Space: `4` tuples to unpack for each rotation -> `O(1)`

Where `n` is the width and `height` of the `matrix`

## Results (Python 3)

**Method 1**: 47 ms, 13.8 MB (68.66%, 74.54%)

**Method 2**: 68 ms, 14 MB (20.26 %, 30.03%)
