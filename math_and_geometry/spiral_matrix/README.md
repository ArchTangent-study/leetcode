# Spiral Matrix ([LC054](https://leetcode.com/problems/spiral-matrix/))
Difficulty: **Medium**

## Problem

Given an `m x n` `matrix`, return *all elements* of the `matrix` in *spiral order*.

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Must work for all shapes (values of `m,n`)
- `1x1` matrix
- **Indexing**: keeping track of proper indexes to uses when traversing

## Procedure

### Method 1: Four Pointer Row, Column Removal

Big Picture: perform `right, down, left, up` passes on the matrix, shifting pointers.
- Traverse topmost row `T`, then remove it.
- Traverse rightmost column `R`, then remove it.
- Traverse bottommost column `B`, then remove it.
- Traverse leftmost column `L`, then remove it.

### Method 2: Four Pointer Row, Column Removal V2

Same as method 1, with a slightly different approach to the `while` loop.

*Note*: this wound up being much faster, despite the small change.

## Results (Python 3)

**Method 1**: 51 ms, 13.9 MB (39.46%, 82.47%)

**Method 2**: 22 ms, 13.9 MB (**99.55%**, **82.47%**)
