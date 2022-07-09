class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Two Pointer Sliding Window w/Dict Counter"""
        target_chars = {}
        for char in s1:
            if char in target_chars:
                target_chars[char] += 1
            else:
                target_chars[char] = 1

        # NOTE: for s1 of length 3, slice from [0:3] (3 not included) and up
        p1, p2 = 0, len(s1)

        # Check each window of s2 for matching permutation.  Return True if found    
        while p2 < len(s2) + 1:
            window_chars = {}
            for char in s2[p1:p2]:
                if char in window_chars:
                    window_chars[char] += 1
                else:
                    window_chars[char] = 1

            if target_chars == window_chars:
                return True

            # Advance window    
            p1 += 1
            p2 += 1

        # No match found for entire window
        return False
