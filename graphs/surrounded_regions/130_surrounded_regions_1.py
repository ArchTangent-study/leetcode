from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Assigned land tiles by { (row, col), contiguous_group } - water is 0
        assigned = {}
        # Set of groups to NOT be captured - connected to border
        non_capture = set()
        # Current group - incremented by 1 for each new one
        group = 0
        # queue of (row, col) land tiles to assign to a group
        to_assign = deque()
        # Find all unexplored land tiles and perform BFS
        for row, tiles in enumerate(board):
             for col, tile in enumerate(tiles):
                coords = (row,col)
                if coords in assigned:
                    continue
                if tile == "X": 
                    assigned[coords] = 0
                else:
                    # Assign new land group and find all contiguous land
                    group += 1
                    assigned[(row,col)] = group
                    to_assign.append(coords)
                    surroundedBfs(coords, board, assigned, to_assign, non_capture, group)

        # Convert all land ("O") that aren't in non-caputure to water ("X")
        for (row,col), group in assigned.items():
            if group not in non_capture:
                board[row][col] = "X"

        return None

def surroundedBfs(coords, board, assigned, to_assign, non_capture, group):
    """BFS helper for Surrounded Regions."""  
    # Used for bounds checks
    last_row, last_col = len(board) - 1, len(board[0]) - 1
    while to_assign:
        # Get land tile and see if it's:
        # (a) in new group (not already explored) and
        # (b) on the edge (non-captured)
        (row,col) = to_assign.popleft()
        if row == 0 or row == last_row or col == 0 or col == last_col:
            non_capture.add(group)
        # Check for contiguous land (same group). Water is group 0
        north = (row-1, col)
        south = (row+1, col)
        west  = (row, col-1)
        east  = (row, col+1)
        if row > 0 and north not in assigned:
            if board[north[0]][north[1]] == "O":
                assigned[north] = group
                to_assign.append(north)
            else:
                assigned[north] = 0
        if row < last_row and south not in assigned:
            if board[south[0]][south[1]] == "O":
                assigned[south] = group
                to_assign.append(south)
            else:
                assigned[south] = 0
        if col > 0 and west not in assigned:
            if board[west[0]][west[1]] == "O":
                assigned[west] = group
                to_assign.append(west)
            else:
                assigned[west] = 0
        if col < last_col and east not in assigned:
            if board[east[0]][east[1]] == "O":
                assigned[east] = group
                to_assign.append(east)
            else:
                assigned[east] = 0
