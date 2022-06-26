# type: ignore

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """BFS from each coast UPWARD, then merge tiles that flow to both.

        Data is stored in (row, column) fashion
        """
        last_row, last_col = len(heights) - 1, len(heights[0]) - 1
        atl_touched = set()
        pac_touched = set()
        # Store (row, col, height) data in queue
        to_explore = deque()

        # Pacific-adjacent: row 0, col 0.  Add tiles to queue and set
        # All values in 1st row
        for col, atl_height in enumerate(heights[0]):
            to_explore.append((0, col, atl_height))
            pac_touched.add((0, col))
        # All values in 1st column
        for row, pac_heights in enumerate(heights):
            if row > 0:
                to_explore.append((row, 0, pac_heights[0]))
                pac_touched.add((row, 0))
        # BFS on all PAC-touching tiles
        pacAtlBfs(heights, to_explore, pac_touched, last_row, last_col)

        # Atlantic-adjacent: row max, col max.  Add tiles to queue and set
        # All values in last row
        for col, atl_height in enumerate(heights[last_row]):
            to_explore.append((last_row, col, atl_height))
            atl_touched.add((last_row, col))
        # All values in last column (up to last row, which is already added)
        for row, atl_heights in enumerate(heights):
            if row < last_row:
                to_explore.append((row, last_col, atl_heights[last_col]))
                atl_touched.add((row, last_col))
        # BFS on all ATL-touching tiles
        pacAtlBfs(heights, to_explore, atl_touched, last_row, last_col)

        # Answer is intersection of tiles that touch ATL and PAC
        # Convert tuple pairs to list pairs
        return [[r,c] for r,c in atl_touched.intersection(pac_touched)]


def pacAtlBfs(heights, to_explore, touched, last_row: int, last_col: int):
    """BFS helper for Pacific-Atlantic problem."""
    while to_explore:
        (row, col, ht) = to_explore.popleft()
        # Add all N,S,W,E tiles that are same level or higher
        # queue holds (row, col, height) tuple
        if row > 0 and (row-1, col) not in touched:
            north_ht = heights[row-1][col]
            if north_ht >= ht:
                touched.add((row-1, col))
                to_explore.append((row-1, col, north_ht))
        if row < last_row and (row+1, col) not in touched:
                south_ht = heights[row+1][col]
                if south_ht >= ht:
                    touched.add((row+1, col))
                    to_explore.append((row+1, col, south_ht))
        if col > 0 and (row, col-1) not in touched:
            west_ht = heights[row][col-1]
            if west_ht >= ht:
                touched.add((row, col-1))
                to_explore.append((row, col-1, west_ht))
        if col < last_col and (row, col+1) not in touched:
                east_ht = heights[row][col+1]
                if east_ht >= ht:
                    touched.add((row, col+1))
                    to_explore.append((row, col+1, east_ht))
