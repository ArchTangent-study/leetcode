# Maximum Length of Binary Tree ([LC104](https://leetcode.com/problems/maximum-depth-of-binary-tree/))
Difficulty: **Easy**

## Problem
Given the `root` of a binary tree, return its **maximum depth**.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- No `root` node: just return `0`

## Procedure

### Method 1: Depth List

Big Picture:
1. If the `root` node is `null`, return `0`
2. Create a common list `depths` to be shared among `root` and all child nodes.
3. Pass current `depth` and `depths` list to `left` and `right` nodes
4. If `left`/`right` child nodes exist, they add current `depth` to `depths` list.
5. Continue recursively until all nodes have been traversed.
6. Return the maximum depth stored in `depths` list.

Thoughts:  this was one of the first LC problems I ever did, and as such the solution is needlessly complex (especially WRT space complexity).  See Method 2 for a much better approach.

Complexity:
- Time: traverse each node only once -> `O(n)`
- Space: add an integer to `depths` for ever node visited -> `O(n)`

### Method 2: Recursion w/DFS

Use depth-first search to recursively update the maximum depth.

Key ideas:
- The maximum depth at *any* `Node` is the maximum depth at either its `left` or `right` nodes, plus 1.

Complexity:
- Time: traverse each node only once -> `O(n)`
- Space: no additional space needed -> `O(1)`

## Results (Python 3)

**Method 1**:  46 ms, 16.4 MB (76.63%, 5.89%)

**Method 2**:  47 ms, 16.3 MB (75.27%, 59.04%)
