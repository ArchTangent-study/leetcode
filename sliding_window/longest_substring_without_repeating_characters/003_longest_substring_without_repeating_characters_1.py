class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Iterative approach w/set deduplication."""
        max_length = 0
        current_length = 0
        current_set = set()

        for start_ix in range(len(s)):
            current_length = 0
            current_set.clear()
            
            for char in s[start_ix:]:
                if char in current_set:
                    # Duplicate found - move to next starting index
                    break
                else:
                    current_length += 1
                    current_set.add(char)      
            # At end of this pass - update max length
            max_length = max(max_length, current_length)
            
        # At end of all iterations
        return max_length
