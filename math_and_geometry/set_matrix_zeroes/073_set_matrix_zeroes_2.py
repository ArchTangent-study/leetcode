from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Return matrix in-place.  Use row and col lists"""
        m = len(matrix)
        n = len(matrix[0])
        rows_to_zeroize = [1] * m
        cols_to_zeroize = [1] * n

        for row, row_data in enumerate(matrix):
            for col, val in enumerate(row_data):
                if val == 0:
                    rows_to_zeroize[row] = 0
                    cols_to_zeroize[col] = 0

        # Apply zeroiziation
        for row, val in enumerate(rows_to_zeroize):
            if val == 0:
                for col in range(n):
                    matrix[row][col] = 0
        for col, val in enumerate(cols_to_zeroize):
            if val == 0:
                for row in range(m):
                    matrix[row][col] = 0
                    