from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Three Pointers w/Two Pointer Closing Window, Deduplication, and Sorting"""
        nums.sort()      
        answer = []
        L = 0
        left_limit = len(nums) - 2
        right_limit = len(nums) - 1
        # Set of first, second numbers already fully explored
        first_nums_explored = set()
        second_nums_explored = set()

        while L < left_limit:
            # Get sum of M, R values to equal `target`
            num_1 = nums[L]
            if num_1 in first_nums_explored:
                L += 1
                continue

            second_nums_explored.clear()
            target = 0 - num_1
            M, R = L + 1, right_limit

            while M < R:
                num_2 = nums[M]
                # If this L,M combination has been fully checked, move to next M
                if num_2 in second_nums_explored:
                    M += 1
                    continue

                num_3 = nums[R]
                mr_sum = num_2 + num_3

                # Add num_2 to set of second numbers explored when M pointer shifts
                if mr_sum == target:
                    answer.append([num_1, num_2, num_3])
                    second_nums_explored.add(num_2)
                    M += 1
                elif mr_sum > target:
                    R -= 1
                else:
                    second_nums_explored.add(num_2)
                    M += 1            

            # Add num_1 to set of first numbers explored when L pointer shifts
            first_nums_explored.add(num_1)
            L += 1

        return answer
