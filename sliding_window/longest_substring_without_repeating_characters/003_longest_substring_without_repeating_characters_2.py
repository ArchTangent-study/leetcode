class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Sliding window w/hashmap"""
        max_length = 0
        # Index from which current substring starts
        start_ix = 0
        # Map of { char : index }
        char_map = {}
        for i, char in enumerate(s):
            # Check for repeat char. If not, add current character
            if char not in char_map:
                char_map[char] = i
            else:
                # Repeat. Update max length and char map starting *after* 1st duplicate
                max_length = max(max_length, i - start_ix)
                duplicate_ix = char_map[char]
                start_ix = duplicate_ix + 1     
                # Reset map with items from start index to current index
                char_map.clear()
                for ix, c in enumerate(s[start_ix: i+1], start=start_ix):
                    char_map[c] = ix
        # End of iteration - check if final substring was the longest
        max_length = max(max_length, len(s) - start_ix)

        return max_length
