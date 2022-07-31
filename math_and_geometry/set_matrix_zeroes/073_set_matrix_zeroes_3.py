from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Return matrix in-place.  Use first row and col as 'to zeroize' lists."""
        m = len(matrix)
        n = len(matrix[0])
        # Indicates whether 0th row will be zeroized.  Needed due to row/col overlap.
        row_0_zeroized = any(val == 0 for val in matrix[0])

        # Start from row 1, since 0th row done above.
        for row in range(1, m):
            for col in range(0, n):
                val = matrix[row][col]
                # Set 0th value in *and* col to 0
                if val == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Apply zeroiziation
        # Rows 1 and up: check if first value in that row is 0
        for row in range(1, m):
            if matrix[row][0] == 0:
                for col in range(1, n):
                    matrix[row][col] = 0
        # Cols 0 and up: check if first value in that col is 0
        for col in range(0, n):
            if matrix[0][col] == 0:
                for row in range(1, m):
                    matrix[row][col] = 0
        # Special case for row 0
        # NOTE: need to be done *after* to avoid contaminating previous calcs
        if row_0_zeroized:
            for col in range(0, n):
                matrix[0][col] = 0
