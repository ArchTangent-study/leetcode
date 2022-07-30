from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Return matrix in-place.  Use row and col sets"""
        m = len(matrix)
        n = len(matrix[0])
        rows_to_zeroize = set()
        cols_to_zeroize = set()

        for row, row_data in enumerate(matrix):
            for col, val in enumerate(row_data):
                if val == 0:
                    rows_to_zeroize.add(row)
                    cols_to_zeroize.add(col)

        # Apply zeroiziation
        for row in rows_to_zeroize:
            for col in range(n):
                matrix[row][col] = 0
        for col in cols_to_zeroize:
            for row in range(m):
                matrix[row][col] = 0
