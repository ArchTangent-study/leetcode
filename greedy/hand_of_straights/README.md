# Hand of Straights ([LC846](https://leetcode.com/problems/hand-of-straights/))
Difficulty: **Medium**

*Note*: This question is the same as ([LC1296](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/))

## Problem

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array hand where `hand[i]` is the value written on the `ith` card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

Constraints:
- `1 <= hand.length <= 10⁴`
- `0 <= hand[i] <= 10⁹`
- `1 <= groupSize <= hand.length`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- `hand` length is `1`

Ideas:
- Sorting in advance
- Hashmap-based counter (or `defaultdict`)

## Procedure

### Method 1: Hash Sequence w/Counter

*Note*: a similar technique to find the start of the sequence is used in Longest Consecutive Sequence (`LC128`).
*Note*: a Python `collections.defaultdict` could also work in place of a normal `dict`.

Big Picture:
1. Collect all values in a Hashmap, used as a counter
2. Find a value that starts a sequence (no value to its left)
3. Count all values in sequence up to groupSize
    - if not enough sequential cards, return `False`
    - remove each card from cards
4. If you get through all cards w/o failing, return `True`

Complexity:
- Time: each `card` is removed as soon as part of sequence -> `O(n)`
- Space: a `dict` that stores all `n` cards -> `O(n)`

## Results (Python 3)

**Method 1**: 358 ms, 15.6 MB (34.07%, **91.89%**)
