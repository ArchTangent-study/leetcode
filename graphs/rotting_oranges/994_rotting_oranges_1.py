from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Use BFS while rot can be spread to fresh oranges.  Uses (row, col) order."""
        minutes = 0
        fresh = 0
        # Use for bounds checks
        last_row, last_col = len(grid) - 1, len(grid[0]) - 1
        # Stores (row, col, turn rotted) of rotten oranges
        rotten = deque()
        explored = set()
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if tile == 2:
                    rotten.append((row, col, 0))
                    explored.add((row, col))
                elif tile == 1:
                    fresh += 1
        # Collect all rotten and propagate rot until no rotten remain
        while rotten:
            # Get rotten orange and update time elapsed
            (row, col, turn_rotted) = rotten.popleft()
            minutes = max(minutes, turn_rotted)
            # Check neighbors for fresh oranges and convert them w/new rot turn
            north = (row-1, col)
            south = (row+1, col)
            west  = (row, col-1)
            east  = (row, col+1)
            if row > 0 and north not in explored:
                explored.add(north)
                if grid[north[0]][north[1]] == 1:
                    rotten.append((*north, turn_rotted+1))
                    fresh -= 1
            if row < last_row and south not in explored:
                explored.add(south)
                if grid[south[0]][south[1]] == 1:
                    rotten.append((*south, turn_rotted+1))
                    fresh -= 1
            if col > 0 and west not in explored:
                explored.add(west)
                if grid[west[0]][west[1]] == 1:
                    rotten.append((*west, turn_rotted+1))
                    fresh -= 1
            if col < last_col and east not in explored:
                explored.add(east)
                if grid[east[0]][east[1]] == 1:
                    rotten.append((*east, turn_rotted+1))
                    fresh -= 1

        # If all rot has spread and fresh oranges remain -> fail.
        if fresh > 0:
            return -1
        else:
            return minutes
            