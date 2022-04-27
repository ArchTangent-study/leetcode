# Invert Binary Tree ([LC226](https://leetcode.com/problems/invert-binary-tree/))
Difficulty: **Easy**

## Problem
Given the root of a binary tree, invert the tree, and return its root.

## Procedure

My plan of action was as follows:
1. Identify the approach.  For this case, you're traversing each node of a tree, so *recursion* is a useful method.
2. Invert the children (subnodes) of a node by swapping their children (swapping the pointers or references to the children).
3. Apply the subnode inversion recursively throughout the tree.

## Results (Python 3)

**Method 1**:  32 ms, 13.9 MB (87.09%, 58.69%)
