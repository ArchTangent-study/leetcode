# Diameter of Binary Tree ([LC543](https://leetcode.com/problems/diameter-of-binary-tree/))
Difficulty: **Easy**

## Problem
Given the `root` of a binary tree, return the *length of the diameter* of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Constraints:
- The number of nodes in the tree is in the range `[1, 10⁴]`.
- `-100 <= Node.val <= 100`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Single node: return `0`
- Unbalanced branches: `left` side and `right` side vary wildly.

Big Picture:
- Diameter at any Node is the highest depth along left node plus highest depth along right node.

## Procedure

### Method 1:  Recursion w/DFS

I used the following logic to come to a solution:

For any given Node in the tree:
- diameter is equal to max depth on left side + max depth on the right side:

```
D = maxDepth(left) + maxDepth(right)
```

- A Node gains depth of 1 if at least one child Node is present.  That is, two extant child Nodes provide 1 depth rather than two:

```python
if (node.left or node.right) { depth = 1 } else { depth = 0 }
```

- Traverse the tree in depth-first fashion (L->R->P).
- At each Node, update the Diameter (D) according to equation above.
- Final diameter is the highest found while traversing the entire tree.

Complexity:
- Time: traverse each node only once -> `O(n)`
- Space: no additional space needed -> `O(1)`

## Other Ideas
I also considered a method that sought the "closest common ancestor", but couldn't get to a well-forumlated solution.  Perhaps for a later time.

## Results (Python 3)

**Method 1**:  48 ms, 16.4 MB (82.98%, 11.02%)
