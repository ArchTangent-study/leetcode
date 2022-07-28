from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Right -> Down -> Left -> Up traversal with pointer shifting."""
        answer = []

        # Left, Right (col), Bottom, Top (row) pointers
        L, R = 0, len(matrix[0])
        T, B = 0, len(matrix)

        while L < R and T < B:
            # Right pass (top row)
            for col in range(L, R):
                answer.append(matrix[T][col])
            T += 1

            # Down pass (right col)
            # NOTE: shift R by -1 for proper indexing
            for row in range(T, B):
                answer.append(matrix[row][R - 1])
            R -= 1

            # NOTE: check L < R and T < B for each horizonal and vertical pass pair
            if not(L < R and T < B):
                break

            # Left pass (bottom row)
            # NOTE: shift L, R, and B by -1 for proper indexing
            for col in range(R - 1, L - 1, -1):
                answer.append(matrix[B - 1][col])
            B -= 1

            # Up pass (left col)
            # NOTE: shift B and T by -1 for proper indexing
            for row in range(B - 1, T - 1, -1):
                answer.append(matrix[row][L])
            L += 1

        return answer
        