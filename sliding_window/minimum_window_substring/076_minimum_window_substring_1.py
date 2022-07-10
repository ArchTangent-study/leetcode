from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Sliding Window - Two Phase."""
        # Last index that the right pointer can touch
        last_ix = len(s) - 1
        # Pointer distance above which p2-p1 must be to contain t. For "aba", min_dist is 1
        min_dist = len(t) - 2  
        # { char : needed } map, with goal of zero of less. Up to 52 chars ("a-z", "A-Z")
        chars_req = defaultdict(int)
        for char in t:
            chars_req[char] += 1

        answer = ""
        p1, p2 = -1, -1
        # Set p1 and p2 by finding *first* window that contains an answer
        for i, char in enumerate(s):
            if char in chars_req:
                chars_req[char] -= 1
                if p1 == -1:
                    p1 = i
                p2 = i
                # `s` has an answer - add it, shift p1 to right to shrink window
                # NOTE: shift p1 by getting char at p1, removing it, then moving p1 up
                if chars_req[char] < 1 and all(v < 1 for v in chars_req.values()):
                    answer = s[p1:p2+1]
                    chars_req[s[p1]] += 1
                    p1 += 1
                    break

        if not answer:
            return ""

        # Shift window, shrinking from left side as new answers are found
        # - if answer found, update it, and shift p1 to the right 
        # - if no answer found, shift p1 and p2 to the right 
        while p2 - p1 > min_dist:
            if all(v < 1 for v in chars_req.values()):
                answer = s[p1:p2+1]
                p1_char = s[p1]
                if p1_char in chars_req:
                    chars_req[p1_char] += 1
                p1 += 1
            else:
                # Only shift p2 right if there's room.  
                if p2 < last_ix:
                    p2 += 1
                    p2_char = s[p2]
                    if p2_char in chars_req:
                        chars_req[p2_char] -= 1
                # Remove current p1 val *before* shifting!
                p1_char = s[p1]
                if p1_char in chars_req:
                    chars_req[p1_char] += 1
                p1 += 1                  

        return answer
