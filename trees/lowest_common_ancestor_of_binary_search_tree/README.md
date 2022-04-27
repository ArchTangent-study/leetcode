# Lowest Common Ancestor of a Binary Search Tree (LC235)
Difficulty: **Easy**

## Problem
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
> The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).

Example 1:
```
          6
     2         8
  0     4   7     9     
       3 5
    
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

Example 2:
```
          6
     2         8
  0     4   7     9     
       3 5

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

Example 3:
```
          2
     1
  
Input: root = [2,1], p = 2, q = 1
Output: 2
```

Constraints:
- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the BST.

## Procedure

### Method 1
Recursively choose the left or right node path based on the relation between `Node.val` and the values of `p` and `q`.  `Node` is the LCA if `p` and `q` are to either side of the node.

Identify three different scenarios:
1. If both `p` and `q` are less than `Node`:  traverse the left node and repeat
2. If both `p` and `q` are greater than `Node`:  traverse the right node and repeat
3. Otherwise, `Node` is the LCA.

### Method 2

Same as method 1, with one change - locally assign each `Node` value before comparing:
```
rv, pv, qv = root.val, p.val, q.val
```
This was about **2x** faster.

## Results (Python 3)

### 1st Method
178 ms, 19.0 MB (5.04%, 23.71%)

### 2nd Method
91 ms, 18.9 MB (67.59%, 23.71%)

## Lessons Learned

**Read the instructions carefully**:  when I first tried this problem, I approached it like I did with other binary trees, failing to notice that this was a Binary *Search* Tree, wwhich allows for a much simpler solution.

**Indirection can be costly**:  I was able to make method 2 much faster (by about 2x) by simply assigning the node value locally, instead of accessing the class variables each time comparisons were performed.
