# Number of Islands ([LC200](https://leetcode.com/problems/number-of-islands/))
Difficulty: Medium

## Problem

Given an `m x n` 2D binary grid grid which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Bounds checks
- Indexing errors
- Properly accessing grid tiles (using `grid[y][x]` vs `grid[x][y]`)

## Procedure

### Method 1: Breadth-First Search

Big Picture:
1. Iterate over `grid`, marking each tile as `explored`.
2. If a land tile is found:
    - increment `island_count` by `1`
    - perform `BFS` (in `up`,`down`,`left`, and `right` directions), collecting all contiguous land tiles and stopping when no neighbors remain.
3. Return `island_count`.

Thoughts: there are definitely some ways to improve memory usage.

## Results (Python 3)

**Method 1**:  391 ms, 28.9 MB (69.27%, 5.01%)
