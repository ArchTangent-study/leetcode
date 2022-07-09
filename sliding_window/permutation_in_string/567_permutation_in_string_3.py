class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Two Pointer Sliding Window w/Counter of Chars Remaining"""
        # { char: count } pairs of chars in target string s1. When all are 0 -> True
        chars_needed = {}
        for char in s1:
            if char in chars_needed:
                chars_needed[char] += 1
            else:
                chars_needed[char] = 1

        # NOTE: for s1 of length 3, slice from [0:3] (3 not included) and up
        p1, p2 = 0, len(s1)

        # Set up initial conditions
        for char in s2[p1:p2]:
            if char in chars_needed:
                chars_needed[char] -= 1

        # Slide window until it goes out of bounds
        while True:
            # Found solution if no more chars are needed (all values are 0)
            match_found = True
            for count in chars_needed.values():
                if count != 0:
                    match_found = False
                    break
            if match_found:
                return True

            # If next window will be in range, set up next values
            if p2 < len(s2):
                # Lower count of right pointer (one less needed)
                p2_char = s2[p2]
                if p2_char in chars_needed:
                    chars_needed[p2_char] -= 1
                # Raise count of left pointer (one more needed)
                p1_char = s2[p1]
                if p1_char in chars_needed:
                    chars_needed[p1_char] += 1
                # Advance window
                p1 += 1
                p2 += 1
            else:
                # End of window
                break

        # No match found for entire window
        return False
