from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate matrix in-place using transpose list."""
        # Center is effectively the 'pivot', used to determine rotation
        last_ix = len(matrix) - 1

        # [(row, col, value) list of values to set
        transfers = []
        for row, row_data in enumerate(matrix):
            for col, val in enumerate(row_data):
                transfers.append((col, last_ix - row, val))

        for (row, col, val) in transfers:
            matrix[row][col] = val    
        