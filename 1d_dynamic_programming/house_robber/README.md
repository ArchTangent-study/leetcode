# House Robber ([LC198](https://leetcode.com/problems/house-robber/))
Difficulty: **Medium**

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array nums representing the amount of money of each house, return *the maximum amount of money you can rob tonight* ***without alerting the police***.

Constraints:
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Can't break into two adjacent houses (must skip 1 after robbing 1)
- only one house: just return `nums[0]` since only one house
- only two houses: just return `max(nums[0], nums[1])` since only one house
- skipping more than one house

## Visualization

The largest number of houses you'll need to skip is `2`.

```
#Houses    House Options
 1          H
 2          H_ ,  _H
 3          H_H , _H_
 4          H__H, H_H_, _H_H
 5          H_H_H, H__H_, _H_H_, _H__H

 ... and so on
```

## Procedure

### Method 1: Iterative DP

Key Idea: use a ***three-house*** sliding window, since the largest space you'll need between robbing houses is `2` (see *Visualization* above).

Big Picture:
1. If only one house, rob that house
2. If two houses, rob the one with more money
3. If three or more houses, gather highest running total using a moving window, starting at `index [2]`.
4. Highest value at any house is the highest of:
    - current house + three houses back
    - current house + two houses back
    - one house back
5. Update the highest value and advance the three-house window forward
6. Return the highest value once all houses have been visited

Complexity:
- Time: traverse each `number` in `nums` once -> `O(n)`
- Space: update `5` varaibles regardless of `nums` length -> `O(1)`

## Results (Python 3)

**Method 1**: 65 ms, 13.9 MB (11.77%, 65.37%)
