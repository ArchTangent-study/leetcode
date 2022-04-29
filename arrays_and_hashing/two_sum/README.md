# Two Sum ([LC001](https://leetcode.com/problems/two-sum/))
Difficulty: **Easy**

## Problem

Given an array of integers `nums` and an integer `target`, return *indices* of the two numbers such that they add up to `target`.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

Constraints:
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

## Procedure

### Method 1: Simple Iteration

This was the most obvious, and likely least efficient, solution.  Still, it's worth exploring, if only to compare against other solutions.

Steps:
1. Assign a `index_1` of `0` and a `index_2` of `1`.
2. Check if `nums[index_1] + nums[index_2] == target`. If so, you're done.  Otherwise, continue.
3. Increment `index_2` and repeat step (2). If `index_2` is out of bounds, move to step (4).
4. Increment `index_1` and `index_2` by 1, and continue from step (2).

The `index_1` and `index_2` values progress as follows until a solution is found:
```
index    1 2            step 1
           1 2          step 2
             1 2        step 3
               1 2      step 4
                 1 2    step 5
nums    [3,5,7,2,5,1]
```
Thoughts:  the solution isn't particularly efficient or elegant, but it works.  Something to build upon in attempt #2.

## Results (Python 3)

**Method 1**:  5491 ms, 15.0 MB (14.03%, 76.86%)
