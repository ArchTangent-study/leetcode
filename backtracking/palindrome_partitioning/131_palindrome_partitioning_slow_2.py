# This gets right answers, but fails on "Time Limit Exceeded"
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
        found = set()
        combos = [[]]
        for substring in substrings:
            for combo in combos:
                test_string = "".join(combo) + substring
                if s.startswith(test_string):
                    val = [*combo, substring]
                    tup = tuple(val)
                    if s == test_string and tup not in found:
                        found.add(tup)
                        answer.append(val)
                    else:
                        to_add.append(val)
            # NOTE: re-use existing to_add list
            combos.extend(to_add)
            to_add.clear()

        return answer
