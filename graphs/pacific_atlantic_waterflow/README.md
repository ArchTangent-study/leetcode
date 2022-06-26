# Pacific Atlantic Waterflow ([LC417](https://leetcode.com/problems/pacific-atlantic-water-flow/))
Difficulty: Medium

## Problem

There is an m x n rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a ***2D list*** *of grid coordinates* `result` *where* `result[i] = [ri, ci]` *denotes that rain water can flow from cell* `(ri, ci)` *to* ***both*** *the Pacific and Atlantic oceans*.

Constraints:
- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 105`

## Thought Process

Ocean-touching tiles are on the edges of the map (`x=0, y=0, x=xdims, y=ydims`).

Edge Cases / Caveats / Pitfalls:
- Empty heights -> N/A as per constraints
- Same height tiles
- Channels

Approaches:
- BFS
- DFS: recursively report whether a given node touches `PAC/ATL` tiles
- Start from corners and work up: `NE` and `SW` corners already flow into both oceans, so start from there and work up
- Start from the *highest points*: they're the most likely to have downflow
- Start from the *coasts*: return values that touch both.

## Procedure

### Method 1: Bottom-Up Breadth-First Search

Key Idea: find the intersection of all tiles that touch both coasts.

Big Picture:
1. Gather all Atlantic coast tiles in an `atlantic` set
2. Gather all Pacific coast tiles in a `pacific` set
3. For each tile on ATL coast, do a `BFS`, adding all neighbors that are *equal to or higher* than current tile.  Add those tiles to the `atlantic` set.
4. For each tile on PAC coast, do a `BFS`, adding all neighbors that are *equal to or higher* than current tile.  Add those tiles to the `pacific` set.
5. Return the intersection of the `atlantic` and `pacific` sets as a list of `[row, col]` coordinates.

Techniques:
- BFS
- Bottom-Up (working backwards)

Complexity:
- Time: Two breadth-first searches -> `O(2n)` -> `O(n)`
- Space: Atlantic and Pacific sets, queue -> `O(3n)` -> `O(n)`

## Results (Python 3)

**Method 1**: 255 ms, 17.7 MB (**99.7%**, 34.87%)
