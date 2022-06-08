# Invert Binary Tree ([LC226](https://leetcode.com/problems/invert-binary-tree/))
Difficulty: **Easy**

## Problem
Given the root of a binary tree, invert the tree, and return its root.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- No `root` node: just return `0`

## Procedure

### Method 1: Recursive w/DFS

Use depth-first search and recursively swap `left` and `right` child nodes.

Big Picture:
1. Invert the children (subnodes) of a node by swapping their children (swapping the pointers or references to the children).
2. Apply the subnode inversion recursively throughout the tree.

Complexity:
- Time: traverse each node only once -> `O(n)`
- Space: no additional space needed -> `O(1)`

## Results (Python 3)

**Method 1**:  32 ms, 13.9 MB (87.09%, 58.69%)
