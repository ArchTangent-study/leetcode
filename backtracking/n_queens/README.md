# N-Queens ([LC051](https://leetcode.com/problems/n-queens/))
Difficulty: **Hard**

## Problem

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the n-queens puzzle*. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

Constraints:
- `1 <= n <= 9`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Impossible solutions (`n=2`)
- Getting output format correct

Ideas:
- Queens attack each other reciprocally: if Q1 can hit Q2, Q2 can hit Q1
- Try every position in the grid
- Find all cells that can be attacked by a Queen from that position
- if there are `n-1` spaces that are unassailable from that spot, this satisfies the requirements.
- Use "mirror images" of working solutions
- Recursively find free spaces after placing a queen, and continue until `n` queens are placed *or* no free spaces remain (recursion)

## Procedure

### Method 1

## Results (Python 3)

**Method 1**:  ms, MB (%, %)
