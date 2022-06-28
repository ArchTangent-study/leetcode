# Surrounded Regions ([LC130](https://leetcode.com/problems/surrounded-regions/))
Difficulty: Medium

## Problem

Given an `m x n` matrix `board` containing `'X'` and `'O'`, *capture all regions that are 4-directionally surrounded by* `'X'`.

A region is **captured** by flipping all `'O'`s into `'X'`s in that surrounded region.

Constraints:
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Border tiles: any border tile or tile connected to one is *not captured*

Big picture: a region is *not* captured if there is at least *one* tile that has neither land nor water on its NSEW edge.  In other words, a region is not captured if at least *one* tile in the region is on the border.

## Procedure

### Method 1: Breadth-First Search w/Non-Capture Groups

Big Picture:
1. Gather all contiguous land tiles by group (also see *Number of Islands* problem)
2. If any member of that group is on the `board` edge, assign group to a `non_capture` set.
3. Once all tiles explored, assign any tiles *not* in the `non_capture` set to water (`"X"`)

## Results (Python 3)

**Method 1**: 322 ms, 19.5 MB (14.86%, 17.74%)
