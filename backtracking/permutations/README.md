# Permutations ([LC046](https://leetcode.com/problems/permutations/))
Difficulty: **Medium**

## Problem

Given an array nums of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

Constraints:
- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## Thought Process

Note: a [permuation](https://en.wikipedia.org/wiki/Permutation) is effectively a rearrangment of a sequence's elements.

Edge Cases / Caveats / Pitfalls:
- getting each number in each possible position
- returning duplicate results

Approaches:
- Populating a zeroized matrix
- Dynamic Programming
- Recursion
- Brute force w/set deduplication

## Procedure

### Method 1: Recursion w/DFS

Key Idea: recursively explore scenarios where each `number` in `nums` is the first among those remaining to be added to a permutation.  Effectively, *numbers take turns going first*.

Big Picture:
1. Iterate over each `number` in `nums`
2. Add `number` to the start of `numbers_so_far`
3. Set `remaining` to the numbers that aren't `number`
4. Recursively call a `dfs()` function to perform steps `1-3` until no numbers are left in `remaining`
5. When `remaining` is empty, add the permutation to `answer`
6. Return `answer` once all permutations exhausted.

Complexity:
- Time: explore `n!` solutions -> `O(n!)`
- Space: store copy of each permutation before adding to `answer` -> `O(n)`

Where:
- `n` is `len(nums)`

### Method 2: Dynamic Programing w/Index Insertion

Key Idea: use previously-calculated permutations to build the next permutations in succession.

Visualization:
```
    1 num   2 nums  3 nums  4 nums
        1     12     312    4312   
              21     321    4321
                     132    4132
                     231    4231
                     123    4123
                     213    4213
                            3412
                            3421
                            1432
                            2431
                            1423
                            2413
                            ... etc
```
Big Picture:
1. Iterate over every `number` in `nums`
2. Iterate over every previously-calculated permutation in `answer`
3. For every possible index in which `number` could be inserted, insert `number` into a copy of the previously-calculated permutation.
4. Add the copy (with inserted `number`) to the `staging` list
5. Once all indexes for `number` have been exhausted, clear `answer` and add new permuations from `staging` area to answer
6. Continue until all `number`s have been checked.
7. Return `answer`

Complexity:
- Time: explore `n!` solutions -> `O(n!)`
- Space: store all possible permuations so far in `staging` list -> `O(n! * n)`

Where:
- `n` is `len(nums)`

### Python Warning

Be careful when initilazing zeroized lists in Python!

If you initialize a `list` of `list`s as follows:
```python
>>> matrix = [ [0] * 3 ] * 4
```
You'll get the following:
```python
>>> matrix
[ [0,0,0], [0,0,0], [0,0,0] ]
```
***However***, if you insert a value into the matrix by indexing, you'll get unusual behavior:
```python

>>> matrix[1][2] = 3

>>> matrix
[ [0,0,3], [0,0,3], [0,0,3] ]
```
Note that **all** of the indexes are overwritten!

Do this instead:
```python
>>> matrix = [ [0] * 3 for _ in range(4) ]
```

## Results (Python 3)

**Method 1**: 70 ms, 14.1 MB (30.03%, 56.74%)

**Method 1**: 63 ms, 14.1 MB (44.50%, 56.74%)
