class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Extract alphanumeric characters from string and convert to lowercase
        new_string = "".join(c for c in s if c.isalnum()).lower()

        forward_iter = iter(new_string)
        reverse_iter = reversed(new_string)

        # Iterate one-by-one over fwd & rev iterators and ensure match
        for c1 in forward_iter:
            c2 = reverse_iter.__next__()
            if c1 != c2:
                return False

        # All checks passed -> it is a palindrome
        return True
    