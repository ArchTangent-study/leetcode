# Subtree of Another Tree ([LC572](https://leetcode.com/problems/subtree-of-another-tree/))
Difficulty: **Easy**

## Problem
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

Constraints:
- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

## Thought Process

Edge Cases:
- `root` and `subRoot` are both `null`
- `root` exists while `subRoot` is `null`
- `subRoot` exists while `root` is `null`
- nodes both exist, but have different values
- a `null` `subRoot` is the sub-tree of *any* tree -> always `true`

## Procedure

### Method 1: Collect Nodes and Compare Slices

This problem builds upon things learned from the **Same Tree** LeetCode exercise ([LC100](https://leetcode.com/problems/same-tree)) [[My Solution](https://github.com/ArchTangent-study/leetcode/tree/main/trees/same_tree)].

The plan of action:
1. Traverse the `root` and `subRoot` trees using *recursion*, collecting their values into respective lists.  Include any `null` children.
2. Compare moving slice "*windows*" of the `root` node list vs the entirety of the `subRoot` node list. The size of each slice is the length of the `subRoot` node list.
3. If a *window* is equal to the `subRoot` node list, return `True` (early exit).  
4. If no *windows* match, return `False`.

*Note*:  Python allows for out-of-bounds (OOB) slice indexes:  the slice will simply be truncated so that all values will be in-bounds.  An example you can try in the terminal:
```
>>> a = [1,2,3,4,5]
>>> a[0:10]
[1, 2, 3, 4, 5]
```
This can be used to solve the problem without fear of going OOB when slicing.

### Method 2: Recursive Comparison

This was **~1.7x** slower than method 1.

Big Picture:
1. `subRoot` is a subtree of `root` if:
    - `root` and `subRoot` are both `null` *OR*
    - `root` and `subRoot` have same values *AND*
    - `root` and `subRoot` have the same children
2. Check each node of `root` against `subRoot` and apply the checks in step `1`.
    - if for any given node in `root`, the result is `true`, then `subRoot` is a subTree of `root` -> return `true`.
    - if all nodes in `root` are traversed without matching `subRoot`, return `false`.

Steps:
1. If the top-level `root` is the same as `subRoot`, early exit with `true`
2. *Recursively* check the child nodes of `root` vs `subRoot` to see if *they* are a match.
    - use *OR logic*, since only *one* of the child nodes needs to match `subRoot`.

## Results (Python 3)

**Method 1**: 117 ms, 15.1 MB (91.78%, 64.85%)

**Method 2**: 197 ms, 15.0 MB (27.99%, 63.91%)
