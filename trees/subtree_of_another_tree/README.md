# Subtree of Another Tree (LC572)
Difficulty: **Easy**

## Problem
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

Example 1:
```
        root
          3         subRoot
     4        5        4
  1     2           1     2
    
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

Example 2:
```
        root
          3         subRoot
     4        5        4
  1     2           1     2
       0 

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

Constraints:
- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

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

## Results (Python 3)

### Method 1
117 ms, 15.1 MB (91.78%, 64.85%)
