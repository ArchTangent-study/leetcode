# Rotting Oranges ([LC994](https://leetcode.com/problems/rotting-oranges/))
Difficulty: Medium

## Problem

You are given an m x n grid where each cell can have one of three values:
- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If this is impossible, return `-1`.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Cases where rot can't spread to a fresh orange
- Case where all oranges are rotten
- Account for cases w/no oranges
- Account for cases where neighboring orange is already rotten
- Properly getting the *minimum* number of *turns*
- How to count `minutes`

Game Plan:
- Track all `fresh` and `rotten` oranges at start
- For every `rotten` orange, spread `rotten` status to any `fresh` orange
- Increment `time` counter *if* at least one orange was converted
- Continue until all oranges are `rotten` or until a turn passes when no fresh orange was converted (unreachable).

## Procedure

### Method 1: Breadth-First Search w/Generation Tracking

Big Picture:
1. Store count of `fresh` oranges and `minutes` elapsed (starting at `0`)
2. Place all `rotten` oranges in a queue with `(row, col, turn_rotted)`
3. Perform BFS with all `rotten` oranges:
    - update `minutes` with the highest of itself and `turn_rotted`
    - spread rot to any `fresh` orange and reducing `fresh` count by `1`.  For any *turned* oranges, their `turn_rotted` is that of the orange that turned them, plus `1`.
4. Once all `rotten` oranges are exhausted, check the `fresh` count
    - if `fresh > 0`, at least one fresh orange remains -> return `-1`.
    - otherwise, return `minutes`

## Results (Python 3)

**Method 1**: 88 ms, 13.9 MB (35.63%, 46.65%)
