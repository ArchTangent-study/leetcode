class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Two Pointer Sliding Window."""
        # L/R pointers, chars covered by them, and span required to expaned
        p1, p2, span = 0, 0, 0
        str_len = len(s)
        # Char count - add when right pointer advances, sub when left pointer advances
        max_count = 0
        count = { s[0]: 0 }

        while p2 < str_len:
            # Is there enough spare k to advance right pointer alone?
            # - if so, advance right pointer by itself
            # - if not, advance both left and right pointer
            right_char = s[p2]
            if right_char in count:
                count[right_char] += 1
            else:
                count[right_char] = 1
                
            span += 1            
            highest_count = max(ct for ct in count.values())       
            
            if span > highest_count + k:
                # Bring left pointer in and lower span
                left_char = s[p1]
                count[left_char] -= 1
                span -= 1
                p1 += 1

            # NOTE: update max_count *after* left pointer adjustment
            if span > max_count:
                max_count = span

            p2 += 1

        return max_count
