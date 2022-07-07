class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Two Pointer Sliding window"""
        max_length = 0
        start_ix, current_ix = 0, 0
        char_set = set()
        while current_ix < len(s):
            char = s[current_ix]
            # Check for repeat of char
            if char in char_set:
                # Update max length
                current_length = current_ix - start_ix
                if current_length > max_length:
                    max_length = current_length 
                # Remove chars from start_ix up to (not including) duplicate
                for i, c in enumerate(s[start_ix:current_ix], start=start_ix):
                    if c == char:
                        # Shift start index
                        start_ix = i + 1
                        break
                    char_set.remove(c)    
            # Add char to set
            char_set.add(char)     
            # Move to next index
            current_ix += 1

        # End of iteration current_ix now at len(s) 
        final_length = current_ix - start_ix
        if final_length > max_length:
            max_length = final_length

        return max_length
        