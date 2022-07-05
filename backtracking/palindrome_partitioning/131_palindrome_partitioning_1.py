from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Recursive DFS backtracking."""
        answer = []

        def dfs(so_far: List[str], incoming: str, remaining: str):
            # If incoming is not palindrome, exit
            if incoming != incoming[-1::-1]:
                return
            # Add new palindromic substring to "so far"
            new_so_far = [*so_far, incoming]
            len_remaining = len(remaining)
            # If no strings remain, all substrings are palindromes
            if len_remaining == 0:
                answer.append(new_so_far)
                return
            # Create partitions for remaining part of string.
            for partition in range(1, len_remaining + 1):
                front = remaining[:partition]
                back = remaining[partition:]
                dfs(new_so_far, front, back)

        # Top level: split string and perform DFS from there
        for partition in range(1, len(s)+1):
            front = s[:partition]
            back = s[partition:]
            dfs([], front, back)

        return answer
