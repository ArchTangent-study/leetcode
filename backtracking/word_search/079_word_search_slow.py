# This version got 5.02%, 12.23% time and space percentiles.
# Uses filtering, but only from the top down. Need to filter entire board first.
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """DFS starting from first letter in word."""
        last_row, last_col = len(board) - 1, len(board[0]) - 1
        first_letter = word[0]
        last_letter_index = len(word) - 1
        word_letters = set(word)
        ignored_tiles = set()

        def dfs(coords, letter_ix, explored) -> bool:
            nonlocal word
            row, col = coords
            letter = word[letter_ix]
            correct_letter = board[row][col] == letter
            # See if tile is next letter. If so, move to adjacent non-ignored tiles
            if not correct_letter:
                return False
            # Base case - at last letter and letter matches -> word found
            if letter_ix == last_letter_index:
                return True
            # Return True if AT LEAST ONE path creates the word
            found_word = False
            north = (row - 1, col)
            south = (row + 1, col)
            west  = (row, col - 1)
            east  = (row, col + 1)
            # NOTE: each path needs its own copy of the set
            if row > 0 and north not in ignored_tiles and north not in explored:
                found_word |= dfs(north, letter_ix + 1, explored | {coords})
            if row < last_row and south not in ignored_tiles and south not in explored:
                found_word |= dfs(south, letter_ix + 1, explored | {coords}) 
            if col > 0 and west not in ignored_tiles and west not in explored:
                found_word |= dfs(west, letter_ix + 1, explored | {coords})
            if col < last_col and east not in ignored_tiles and east not in explored:
                found_word |= dfs(east, letter_ix + 1, explored | {coords}) 

            return found_word

        for row, tiles in enumerate(board):
            for col, tile in enumerate(tiles):
                # Filter letters
                if tile not in word_letters:
                    ignored_tiles.add((row, col))
                # If tile starts the word, try DFS starting from that letter
                if tile == first_letter:
                    # NOTE: start from depth 0, first letter, at tile's coords
                    found = dfs((row, col), 0, set())
                    if found:
                        return True

        return False
