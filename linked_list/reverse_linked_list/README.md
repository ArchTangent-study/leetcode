# Reverse Linked List ([LC206](https://leetcode.com/problems/reverse-linked-list/))
Difficulty: **Easy**

## Problem

Given the `head` of a singly linked list, reverse the list, and return the *reversed list*.

Constraints:
- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- null `head` -> return `null`
- Single node should return itself
- First node (`head`) should have `next` as null at end of calculation
- Exit condition: when do we stop reversing?  When `next` is null

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

## Visualization

Where `n` is `null`:
```
Go from:
     1 > 2 > 3 > 4 > 5
To:
     5 > 4 > 3 > 2 > 1

        1 > 2   becomes
    n < 1
        2 > 3   becomes
    1 < 2
        3 > 4   becomes
    5 < 4
        5 > n   becomes
    4 < 5
```

## Procedure

### Method 1: Recursive

This one gave me more trouble than I anticipated.

The process:
1. If the `head` is null or `head.next` is null, simply return `head` (accounts for cases where there is zero or one nodes).
2. Recursively call steps `3` to `5` for each node:
3. If the `node.next` is None, set `node.next = prev` and return `node`.
4. Store `node.next` in a temporary `original_next` value as a copy.
5. Set `node.next = prev`.

Thoughts: this can definitely be cleaned up a bit (deduplication, etc.), but it works.

### Method 2: Recursive (Improved)

Same as method 1, but with less redundant code.

This was **~20%** faster than method 1.

### Method 3: Iterative (Follow-Up)

This is similar logic to method 2, but contained in a `while` loop rather than using recursion.

Thoughts: this wasn't particularly fast, but it highly memory efficient.

## Results (Python 3)

**Method 1**: 63 ms, 20.4 MB (21.66%, 20.4%)

**Method 2**: 52 ms, 20.4 MB (43.07%, 9.56%)

**Method 3**: 80 ms, 15.4 MB (5.08%, 15.4%)
