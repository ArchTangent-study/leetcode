# Set Matrix Zeroes ([LC073](https://leetcode.com/problems/set-matrix-zeroes/))
Difficulty: **Medium**

## Problem

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`s.

You must do it **in place**.

Constraints:
- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2³¹ <= matrix[i][j] <= 2³¹ - 1`

Follow up:
- A straightforward solution using `O(mn)` space is probably a bad idea.
- A simple improvement uses `O(m + n)` space, but still not the best solution.
- Could you devise a constant space (`O(1)`) solution?

## Thought Process

Edge Cases / Caveats / Pitfalls:
- `m` or `n` equal to `1`
- get entire `row` and `col`, not just neighbors

Ideas:
- convert entire rows and columns *at once*

## Procedure

### Method 1: Two-Pass Delayed Zeroization with Row/Col Set

Key Idea: use two sets, and two passes over the `matrix`.

Big Picture:
1. Use set of rows/columns to be converted (`rows_to_zeroize`, `cols_to_zeroize`)
2. First pass finds the row/col of any zero values
3. Second pass traverses:
    - each `col` for every `row` in `rows_to_zeroize`
    - each `row` for every `col` in `cols_to_zeroize`
    - and sets each `(row,col)` value in `matrix` to `0`

Complexity:
- Time: Two passes -> `O(2n)` -> `O(n)`
- Space: `O(m + n)`

Thoughts: this was ***incredibly*** fast despite not being optimally space efficient.

## Results (Python 3)

**Method 1**:  119 ms, 14.7 MB (**99.78%**, **90.66%**)
