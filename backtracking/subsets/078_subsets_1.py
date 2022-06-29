from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Account for empty member of power set
        answer = [[]]
        subs = set()
        to_add = []

        for n in nums:
            # Can be either int or tuple(int)
            for subgroup in subs:
                if type(subgroup) == int:
                    to_add.append((subgroup, n))
                else:
                    to_add.append((*subgroup, n))
            # Add own value to set
            subs.add(n)
            # Add new groups
            for sublist in to_add:
                subs.add(sublist)
            # Clear list to re-use
            to_add.clear()

        for s in subs:
            if type(s) == int:
                answer.append([s])
            else:
                answer.append([*s])
        return answer
