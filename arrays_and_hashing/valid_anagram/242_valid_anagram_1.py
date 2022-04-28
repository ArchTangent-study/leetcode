# type: ignore
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Determines if `t` is an anagram of `s`.  Returns False if:

        1. `s` and `t` are of different lengths (`t` cannot be an anagram)
        2. Any letter in `t` is not in `s`
        3. Any letters in `s` are "unused" by `t`: counter values are > 0
        """
        if len(s) != len(t):
             return False

        counter = defaultdict(int)

        for ltr in s:
            counter[ltr] += 1

        for ltr in t:
            match counter.get(ltr):
                # Letter in `s` is not in `t`
                case None:
                    return False
                # Letter is in `s`, but `t` has too many instances
                case 0:
                    return False
                # Lower count for the given letter in `s`
                case _:
                    counter[ltr] -= 1

        return True
