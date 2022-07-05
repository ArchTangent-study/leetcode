# Gets right answers, but has "memory limit exceeded" on long strings like "cbbacabbcdd"
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Dynamic Programming solution."""
        answer = []
        # Get substrings ("a", "aa", "b")
        to_add = []
        substrings = [""]   # Empty string needed for DP
        for char in s:
            for substring in substrings:
                to_add.append(substring + char)
            substrings.extend(to_add)
            to_add.clear()
        # Keep only palindromic substrings that are non-empty
        substrings = [subs for subs in substrings if subs == subs[-1::-1]]
        substrings.remove("")

        # Combinations of palindromic substrings
        combos = [[]]
        for substring in substrings:
            for combo in combos:
                to_add.append([*combo, substring])
            # NOTE: re-use existing to_add list
            combos.extend(to_add)
            to_add.clear()

        # Add any combination to answer if its partitions combine equal input string
        # e.g. for input "aab", substrings "a" + "ab" are palindromes that equal "aab"
        for combo in combos:
            if "".join(combo) == s:
                answer.append(combo)

        return answer