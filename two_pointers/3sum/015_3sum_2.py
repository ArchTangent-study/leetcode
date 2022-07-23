from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Three Pointers w/Two Pointer Closing Window, Int Deduplication, and Sorting"""
        nums.sort()
        answer = []
        L = 0
        left_limit = len(nums) - 2
        right_limit = len(nums) - 1
        # Previous First, Second numbers (-100001 is outside of constraints)
        previous_first_num = -100001    
        previous_second_num = -100001

        while L < left_limit:
            # Get sum of M, R values to equal `target`
            num_1 = nums[L]
            if num_1 == previous_first_num:
                L += 1
                continue

            previous_second_num = -100001
            target = 0 - num_1
            M, R = L + 1, right_limit

            while M < R:
                num_2 = nums[M]
                # If this L,M combination has been fully checked, move to next M
                if num_2 == previous_second_num:
                    M += 1
                    continue

                num_3 = nums[R]
                mr_sum = num_2 + num_3

                # Make num_2 previous second number when M pointer shifts
                if mr_sum == target:
                    previous_second_num = num_2
                    answer.append([num_1, num_2, num_3])
                    M += 1
                elif mr_sum > target:
                    R -= 1
                else:
                    previous_second_num = num_2
                    M += 1            

            # Make num_1 previous first number when L pointer shifts
            previous_first_num = num_1
            L += 1

        return answer
