from typing import Dict, List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Table of {sorted_string: [anagram1, anagram2, ..,]} data
        # Note: defaultdict(list) is another option here
        matches: Dict[str, List] = {}

        # Sort in alphabetical order for easy comparison
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in matches:
                matches[sorted_string].append(string)
            else:
                matches[sorted_string] = [string]

        return [match_list for match_list in matches.values()]
