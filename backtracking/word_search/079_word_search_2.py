from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """DFS with preliminary filtering and early exit."""
        last_row, last_col = len(board) - 1, len(board[0]) - 1
        first_letter = word[0]
        last_letter_index = len(word) - 1
        # Count each letter in word, decrementing for each time found in board
        word_letters = { letter: word.count(letter) for letter in word }
        ignored_tiles = set()
        start_tiles = []

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

        # Filter pass
        for row, tiles in enumerate(board):
            for col, tile in enumerate(tiles):
                # Filter letters
                if tile not in word_letters:
                    ignored_tiles.add((row, col))
                    continue
                # Decrement letter count
                word_letters[tile] -= 1
                # Add to list to be checked in search pass
                if tile == first_letter:
                    start_tiles.append((row, col))

        # Early exit - stop if board doesn't have enough of word's letters
        for letter_count in word_letters.values():
            if letter_count > 0:
                return False

        # Search pass
        # NOTE: start from depth 0, first letter, at tile's coords
        for coords in start_tiles:
            found = dfs(coords, 0, set())
            if found:
                return True

        return False
        