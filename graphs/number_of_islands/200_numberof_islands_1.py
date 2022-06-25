#type: ignore

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:     
        """Note: y is rows; x is cols, accessed via grid in y,x order."""
        island_count = 0
        explored = set()

        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                coords = (x,y)
                if coords in explored:
                    continue
                explored.add(coords)
                # If land, use BFS to find contiguous land tiles
                if tile == "1":
                    island_count += 1
                    addContiguousLand(x, y, grid, explored)

        return island_count


def addContiguousLand(cx: int, cy: int, grid: List[List[str]], explored: set):
    """Breadth-first search helper function. Note: need to check above tiles."""
    xdims, ydims = len(grid[0]), len(grid)
    # Add up, down, left, and right neighbors
    neighbors = deque([(cx,cy-1), (cx,cy+1), (cx-1,cy), (cx+1,cy)])
    while neighbors:
        (x,y) = neighbors.popleft()
        # Skip if already explored or not in bounds
        if (x,y) in explored:
            continue
        explored.add((x,y))
        if not inBounds(x, y, xdims, ydims):
            continue
        # If neighbor is land, check its U/D/L/R neighbors for contiguous land
        if grid[y][x] == "1":
            neighbors.append((x, y-1))
            neighbors.append((x, y+1))
            neighbors.append((x-1, y))
            neighbors.append((x+1, y))                


def inBounds(x: int, y: int, xdims: int, ydims: int) -> bool:
    """Helper to ensure an (x,y) coordinate is in bounds."""
    return x > -1 and y > -1 and x < xdims and y < ydims
