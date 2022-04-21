# Diameter of Binary Tree (LC543)
Difficulty: **Easy**

## Problem
Given the `root` of a binary tree, return the *length of the diameter* of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1
```
Input:  root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

        1       
    2       3   
 4     5
```

Example 2
```
Input:  root = [1,2]
Output: 1
```

Constraints:
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

## Procedure
I used the following logic to come to a solution:

For any given Node in the tree:
- diameter is equal to max depth on left side + max depth on the right side:
```
D = maxDepth(left) + maxDepth(right)
```
- A Node gains depth of 1 if at least one child Node is present.  That is, two extant child Nodes provide 1 depth rather than two:
```
if (node.left OR node.right) { depth = 1 } else { depth = 0 }
```
- Traverse the tree in depth-first fashion (L->R->P).
- At each Node, update the Diameter (D) according to equation above.
- Final diameter is the highest found while traversing the entire tree.

I also considered a method that sought the "closest common ancestor", but couldn't get a grip on the solution.  Perhaps for a later time.

## Results (Python 3)

### Method 1
48 ms, 16.4 MB (82.98%, 11.02%)
