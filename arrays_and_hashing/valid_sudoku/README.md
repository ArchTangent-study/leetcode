# Valid Sudoku ([LC036](https://leetcode.com/problems/valid-sudoku/))
Difficulty: **Medium**

## Problem
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following **rules**:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is ***not necessarily solvable***.
- Only the filled cells need to be validated according to the mentioned rules.

Constraints:
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Not accounting for blank space `"."`
- Handling the nine sub boxes (how to properly index them)

## Procedure

### Method 1: Set Duplicate Detection

Big Picture

Use `13` sets to track duplicates for the following contexts:
1. `row` context: every number in each subarray in the `board`. The `1` row set is cleared at the start of every new row.
2. `column` context: each number in the row has its own column, and is added to one of `9` `column` sets based on its index in the row.
3. `box` context: Every three numbers in a row, a new box is entered (`box_index = row_index // 3`).  Every three rows, each `box` set is reset.  There are `3` box sets active at a given time.

If at any point, a duplicate value is found in a set, return `False`.  If the entire `board` is traversed without a duplicate being found, return `True`.

## Results (Python 3)

**Method 1**: 183 ms, 13.9 MB (17.22%, 81.50%)
