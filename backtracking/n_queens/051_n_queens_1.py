from typing import List, Tuple

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """Recursive backtracking approach.  Place Queens where others can't them."""
        if n == 1:
            return [["Q"]]
        answer = []
        # positions of valid queen positions to be converted into strings
        valid_queens = []

        def assign_queen(board: List, row: int, n: int):
            """Recursively place new Queens in increasing rows"""
            for col in range(n):
                # Try to place new queen at (row, col) against ALL current queens
                # If able to place, continue recursively with queen in next row
                if queen_is_blocked(row, col, board):
                    continue
                else:
                    new_board = [*board, (row, col)]
                    # If at the last row of the board, it's a valid board
                    if row == n-1:
                        valid_queens.append(new_board)
                        return
                    # Continue at next row using copy of board with new queen added
                    assign_queen(new_board, row+1, n)
            # Entire row traversed with no safe place found - return
            return

        # Start with a Queen (Q0) in each column of the top row (row 0)
        for col in range(n):
            starting_board = [(0, col)]
            # Place other Queens (Q1...Qn) in each column of the nth row, start w/row 1
            assign_queen(starting_board, 1, n)

        # Convert groups of valid queens into answer format (one Queen per row)
        # Assign "Q" to appropriate column of "...."
        for coord_list in valid_queens:
            sub_answer = []
            for (_, col) in coord_list:
                row_data = "." * col + "Q" + "." * (n-1-col)
                sub_answer.append(row_data)
            answer.append(sub_answer)

        return answer
    
def queen_is_blocked(row: int, col: int, board: List[Tuple[int, int]]) -> bool:
    """Queen is in range if within horizonal, vertical, or diagonal."""
    for qrow, qcol in board:
        if row == qrow or col == qcol or abs(row - qrow) == abs(col - qcol):
            return True
    return False