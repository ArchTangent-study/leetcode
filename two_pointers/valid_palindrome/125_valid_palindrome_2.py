class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Two pointer approach. Remove all non-alphanumeric chars and make lowercase."""
        L, R = 0, len(s) - 1

        while L <= R:
            c1, c2 = s[L], s[R]
            match c1.isalnum(), c2.isalnum():
                case True, True:
                    if c1.lower() != c2.lower():
                        return False
                    L += 1
                    R -= 1
                case True, False:
                    R -= 1
                    continue
                case False, True:
                    L += 1
                    continue
                case False, False:
                    L += 1
                    R -= 1 

        # Traversed w/o error -> palindrome
        return True
