from typing import List, Set, Tuple
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Breadth first search, with coordinates in (row, col) order."""
        # Default area is 0
        answer = 0
        explored = set()

        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                coords = (row, col)
                # Get area if tile is land (1) and not already explored
                if tile == 1 and coords not in explored:
                    # Add tile to set
                    explored.add(coords)
                    # Keep highest contiguous land mass
                    answer = max(answer, islandArea(coords, grid, explored))

        return answer

def islandArea(coords: Tuple[int, int], grid: List[List[int]], explored: Set) -> int:
    """BFS helper for maxAreaOfIsland. Get largest contiguous land area."""
    # Last row and col used for bounds checks (instead of separate function)
    last_row, last_col = len(grid) - 1, len(grid[0]) - 1
    area = 0
    island_tiles = deque([coords])
    while island_tiles:
        # This is a land tile -> increment area by 1
        row, col = island_tiles.popleft()
        area += 1
        # Check in-bounds, unexplored adjacent tiles for land.
        # Add to set and queue if they are.
        north = (row-1, col)
        south = (row+1, col)
        west =  (row, col-1)
        east =  (row, col+1)
        #  In bounds   ----- unexplored ----     ---------- is land ----------
        if row > 0 and north not in explored and grid[north[0]][north[1]] == 1:
            island_tiles.append(north)
            explored.add(north)
        if row < last_row and south not in explored and grid[south[0]][south[1]] == 1:
            island_tiles.append(south)
            explored.add(south)
        if col > 0 and west not in explored and grid[west[0]][west[1]] == 1:
            island_tiles.append(west)
            explored.add(west)
        if col < last_col and east not in explored and grid[east[0]][east[1]] == 1:
            island_tiles.append(east)
            explored.add(east)

    return area    
