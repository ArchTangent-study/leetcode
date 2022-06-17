from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 overall conexts: row(horizontal), column (vertical), box in MxN array
        # Row covers [0:8] in 2nd dimension (N) - need only one map
        row = set()
        # Box covers [0:2] [3:5] [6:8] in N dimension for every 3 Ms traversed
        box = [set() for i in range(3)]
        # Column covers a single N for each number in M dimension - need 9 maps
        column = [set() for i in range(9)]

        # Reset every three N arrays
        box_reset = 3

        # Note: don't need to track the row index (since row context is reset each row)
        for subarray in board:
            for (n, number) in enumerate(subarray):
                # No number (blank space)
                if number == ".":
                    continue

                if number in row:
                    return False
                row.add(number)

                if number in column[n]:
                    return False
                column[n].add(number)

                # Which of three boxes you're in (each box is 3x3)
                box_index = n // 3
                if number in box[box_index]:
                    return False
                box[box_index].add(number)

            # Clear row data every loop for reuse
            row.clear()
            # Every three M indexes, clear the boxes
            box_reset -= 1
            if box_reset == 0:
                box =  [set() for i in range(3)]
                box_reset = 3

        # If no duplicates found, it's valid
        return True
        