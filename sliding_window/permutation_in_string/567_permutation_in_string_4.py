class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Two Pointer Sliding Window w/List Counter (goal: all zeroes)"""
        # Up to 26 chars ("a"-"z") allowed
        counter = [0] * 26
        m, n = len(s1), len(s2)

        # Setup phase: cover all `m` letters in s1.
        for char in s1:
            counter[ord(char) - ord("a")] += 1
        for char in s2[:m]:
            counter[ord(char) - ord("a")] -= 1

        if all(c == 0 for c in counter):
            return True

        # Iteration phase - with enumerate, have to start at index `m`
        for i, char in enumerate(s2[m:n], start=m):
            # Add incoming s2 character by decrementing count
            counter[ord(char) - ord("a")] -= 1
            # Remove outgoing s2 character by incrementing count
            counter[ord(s2[i-m]) - ord("a")] += 1

            # Check for anagram
            if all(c == 0 for c in counter):
                return True

        # No anagram found
        return False
        