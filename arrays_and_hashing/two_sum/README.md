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

### Method 2: Sorted List (Low-to-High)

The structure is similar to method 1, with some key changes:

1. A new list, `sorted_nums`, is created from `nums`, sorted from low to high
2. Perform searching algorithm on the sorted list, getting the *numbers* that sum up to `target`.
3. An early exit condition is introduced: if `target > sum(lowest_val, highest_val)`, there's no way that `target` can be within the range -> move to the next range. This works particularly well with ranges that contain negative numbers.
4. Since the algorithm (a) returns *numbers*, and (b) operates on a sorted list, the *indexes* still need to be found in the *original* list.
5. Find the indexes of the numbers in the *original* `nums` list by returning the indexes from the left *and* right sides.  This is necessary because if both numbers are the same (e.g. `3` and `3`), the return values will have the same index (the *wrong* answer).

Thoughts: this was *significantly* faster (almost 25x) than method 1, and demonstrates that doing some work up front (sorting) can wind up *saving* time on later calculations.  Still, I feel there's a better way.

*Note*: the right indexing method was found on [StackOverflow](https://stackoverflow.com/questions/6890170/how-to-find-the-last-occurrence-of-an-item-in-a-python-list).

### Method 3: Dictionary

A simple and elegant solution that I found online.  The key concepts:

1. Create an empty hashmap (`sum_table`) to store { target_number : 1st_index } pairs.
2. Start with the equation: `target = num1 + num2`.
3. Rearrange: `num2 = target - num1`.
4. Iterate over each `num1` in list of `nums`, keeping track of its index.
5. For each `num1` in list of `nums`:
    - track the index: `index_1`
    - calculate `num2` using above equation
    - if `num1` is in `sum_table`: get and return its index, along with `num1`'s index. *Note*: this step must come before the next one.
    - store { `num2`: `index_2` } pairs in `sum_table`

This method requires no sorting; only an additional dictionary (hash map) is required.  Faster, but uses more memory.

## Results (Python 3)

**Method 1**:  5491 ms, 15.0 MB (14.03%, 76.86%)

**Method 2**:  223 ms, 15.0 MB (36.98%, 76.80%)

**Method 3**:  102 ms, 15.5 MB (51.51%, 9.61%)

### Lessons learned
Account for *all* inputs, including negative values.  An earlier attempt at a solution (sorting from high to low) was erroneous because it didn't account for them.
