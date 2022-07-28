from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate matrix in-place w/Outside-in Ring Rotation and Tuple Unpacking."""
        # Key idea: rotate 1st n-1 values, then shift row and col by +1
        n = len(matrix)
        to_rotate = n-1
        c1_start = 0
        r1 = 0

        while to_rotate > 0:
            for c1 in range(c1_start, c1_start + to_rotate):
                r2, c2 = c1, n-1-r1
                r3, c3 = c2, n-1-r2
                r4, c4 = c3, n-1-r3

                # Transpose in-place            
                matrix[r2][c2], matrix[r3][c3], matrix[r4][c4], matrix[r1][c1] = \
                    matrix[r1][c1], matrix[r2][c2], matrix[r3][c3], matrix[r4][c4]

            to_rotate -= 2
            c1_start += 1
            r1 += 1
            