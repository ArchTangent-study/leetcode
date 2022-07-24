from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Binary Search based on width of L/R sides."""
        # Get width of left side required to split combined array evenly
        # - For even: left side = right side = combined_len // 2
        # - For odd : left side = combined_len // 2; right_side = left side + 1
        combined_length = len(nums1) + len(nums2)
        left_width = combined_length // 2
        even = combined_length % 2 == 0

        # Highest and Lowest values per constraints
        LOW, HIGH = -10**6, 10**6

        # List A is shorter of the two lists
        listA, listB, lenA, lenB = nums1, nums2, len(nums1), len(nums2)
        if lenA > lenB:
            listA, listB = listB, listA
            lenA, lenB = lenB, lenA

        # Scan for width where highest of left side is < lowest of right side
        # Use the shorter list for binary search (fewer searches needed)
        L1, R1 = 0, len(listA)
        while L1 <= R1:
            # M1 is number of values taken from listA; M2 is that for listB
            M1 = (L1 + R1) // 2
            M2 = left_width - M1

            # Compare highest of both left slices vs lowest of both right slices
            # NOTE: account for empty slices by assigning LOW for left, HIGH for right
            highA = listA[M1 - 1] if listA and M1 > 0 else LOW
            highB = listB[M2 - 1] if listB and M2 > 0 else LOW
            lowA  = listA[M1] if M1 < lenA else HIGH
            lowB  = listB[M2] if M2 < lenB else HIGH
            lowAB = min(lowA, lowB)

            if highA > lowAB:
                # Too many values in listA - adjust M1 down
                R1 = M1 - 1
                continue
            elif highB > lowAB:
                # Too many values in listB - adjust M1 up (and thereby M2 down)
                L1 = M1 + 1
                continue
                
            # If left/right sides are evenly split, find median based on even/odd
            # NOTE: need float division (* 0.5 or / 2 vice // 2) ; watch order of operations
            if even:
                return (max(highA, highB) + lowAB) * 0.5
            else:
                return lowAB

        # Empty list will have median of 0.0
        return 0.0
