from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Table of {(int, int, ...): [match1, match2, ..,]} data} 
        # Key is a 26-tuple of the a-z letter count of each string (inc. zero)
        matches =  defaultdict(list)

        for string in strs:
            # Letters a-z, defaulted to count of 0. `ord('z') + 1` to include z
            letter_counter = {chr(c): 0 for c in range(ord('a'), ord('z') + 1) }
            for character in string:
                letter_counter[character] += 1
            # Collect the letter counts (inc. zero) in a hashable tuple
            letter_count = tuple(count for count in letter_counter.values())
            # Add string to list of matches for given letter count
            matches[letter_count].append(string)

        return [match_list for match_list in matches.values()]
