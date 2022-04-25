# Same Tree (LC100)
Difficulty: **Easy**

## Problem
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
```
    1           1
 2     3     2     3     

Input: p = [1,2,3], q = [1,2,3]
Output: true
```
Example 2:
```
    1       1
 2             2     

Input: p = [1,2], q = [1,null,2]
Output: false
```
Example 3:
```
    1           1
 2     3     2     3    

Input: p = [1,2,1], q = [1,1,2]
Output: false
```
## Procedure

### Method 1: Simple List Comparison

The first way that came to mind.  The plan of action:
1. Identify *recursion* as the main approach.  
2. Store lists for both `p` and `q` trees, tracking the *index* of the last node added.
3. Recursively traverse both trees, adding each node value to their designated lists. Each node adds its own value *before* add those of its left/right child nodes.
4. Once both trees have been fully traversed, compare the lists.
5. If lists are equal, the trees are the same (return `True`).  If not, the trees are not the same (return `False`).

The problem with this approach is that is requires *full traversal* of *both* trees before comparison occurs.  There's certainly a way to each each node as they are encountered, allowing for an optimal *early exit* if a given node pair doesn't match.

### Method 2: Sequential List Comparison

Builds upon method 1.  The differences:
1. Traverse tree `p` in its entirety first.
2. Store an index (`p_index`) for the `active` node in tree `q`.
3. Traverse tree `q`.
4. For each node in `q`: (a) compare its value against the value in `p[p_index]`, and (b) increment the index.
5. If at any index the values are not equal, the trees are not equal (return `False`).
6. If the entire `q` tree is traversed w/o failure, the trees are the same (return `True`).

This solution wound up being even *slower* than method 1.  Perhaps it would be faster in certain scenarios, but at least for LeetCode, it isn't.

There has to be a better way:  it would be ideal to check the `nth` node of each tree *as they are encountered*.  This would require far less memory, and exit as soon as the first unmatched pair occurs.

### Method 3: Paired Recursion

Well, turns out there was a better way!  It was a struggle to find the right way to compare `p` and `q` one node at a time, without using two stacks (which would have worked, but been far less elegant and efficient).  All that's needed is to...call the `isSameTree()` function recursively.

One submission failed due to a runtime error.  The cause: an incomplete early exit. This:
```
        if p is None:
            return q is None
```
instead of this:
```
        if p is None:
            return q is None
        if q is None:
            return p is None
```
The first example doesn't account for the case where `p` is a valid node while `q` is not.  Despite the minor setback, this was by far the best (and most succinct) of my three solutions.

## Results (Python 3)

### Method 1
31 ms, 14.0 MB (87.21%, 31.58%)

### Method 2
43 ms, 14.0 MB (47.31%, 31.58%)

### Method 3
26 ms, 13.9 MB (96.15%, 77.02%)
