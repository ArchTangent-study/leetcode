# Invert Binary Tree (LC226)
Difficulty: **Easy**

## Problem
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

Example 2:
```
Input: root = [2,1,3]
Output: [2,3,1]
```

Example 3:
```
Input: root = []
Output: []
```
## Procedure

My plan of action was as follows:
1. Identify the approach.  For this case, you're traversing each node of a tree, so *recursion* is a useful method.
2. Invert the children (subnodes) of a node by swapping their children (swapping the pointers or references to the children).
3. Apply the subnode inversion recursively throughout the tree.

## Results (Python 3)

### Method 1
32 ms, 13.9 MB (87.09%, 58.69%)
