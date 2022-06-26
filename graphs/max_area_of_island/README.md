# Max Area of Island ([LC695](https://leetcode.com/problems/max-area-of-island/))
Difficulty: Medium

## Problem

You are given an `m x n `binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return the *maximum* ***area*** *of an island in* `grid`. If there is no island, return `0`.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`.

## Thought Process

Can use a similar approach as used in *Number of Islands* [LC200](https://leetcode.com/problems/number-of-islands/)

Edge Cases / Caveats / Pitfalls:
- No grid -> N/A as per constraints
- No islands -> return `0`
- Same-size islands

Approaches:
- Breadth-First Search
- Depth-First Search

## Procedure

### Method 1: Breadth-First Search

Big Picture:
1. Iterate over unexplored tiles in `grid`
2. If a tile is land, perform `BFS` with that tile:
    - collect and count all contiguous land tiles (including starting tile)
    - return the contiguous count (`area`)
3. Compare the `area` from `BFS` with `highest_area` found so far, and keep maximum
4. Once entire `grid` traversed, return `highest_area`

Thoughts:  this could be made faster by using the same `deque` (queue) repeatedly, rather than creating a new one every time a new landmass is found.

Complexity:
- Time: explore each tile only once -> `O(m * n)`
- Space: a `set` and `queue` holding at worst `m x n` tiles -> `O(m * n)`

## Results (Python 3)

**Method 1**: 246 ms, 14.5 MB (29.88%, 79.11%)
