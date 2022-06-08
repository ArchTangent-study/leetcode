# Balanced Binary Tree ([LC110](https://leetcode.com/problems/balanced-binary-tree/))
Difficulty: **Easy**

## Problem
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Constraints:
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10⁴ <= Node.val <= 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- No nodes: return `True`
- Single node: return `False`
- Must be sure to check for balance at *every* node.

Big Picture:
- A given node is balanced if  both its `left` and `right` nodes are balanced.

## Procedure

### Method 1: Recursion w/DFS

This problem builds upon things learned from other LeetCode exercises, in particular finding the maximum depth of a binary tree ([LC104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)) [[My Solution](https://github.com/ArchTangent-study/leetcode/tree/main/trees/maximum_depth_of_binary_tree)].

Steps:
1. Identify the best approach.  Since we will need to perform the same function (getting L/R node depth for each child), this as a good candidate for *recursion*.
2. Store a top-level `balanced` variable for early exit.  Since the scenario fails if *any* node has unbalanced depth, it makes sense to exit at the *first instance* of this occurring.
3. Find the *max node depth* on the *left* and *right* sides of each node.
4. Compare left depth vs right depth.  If the difference is greater than 1, then the check fails and the tree is *not* balanced.  
5. If the entire tree is traversed without any unbalanced L/R sides, the tree is balanced (return `True`).  Otherwise, it is not (return `False`).

Complexity:
- Time: traverse each node only once -> `O(n)`
- Space: store integers for `left` and `right` depth -> `O(1)`

## Results (Python 3)

**Method 1**:  68 ms, 18.6 MB (58.86%, 90.64%)
