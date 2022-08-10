# Task Scheduler ([LC621](https://leetcode.com/problems/task-scheduler/))
Difficulty: **Medium**

## Problem

Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a *non-negative* integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return *the least number of units of times that the CPU will take to finish all the given tasks*.

Constraints:
- `1 <= task.length <= 10⁴`
- `tasks[i]` is upper-case English letter.
- The integer `n` is in the range `[0, 100]`.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Proper use of min heap:  use `(ready_time, task)`, not `(task, ready_time)`.  IOW, the tasks should be sorted by *time*, not by *task*
- Tasks can be done in any order:  don't idle (consuming a time unit) unless there's nothing else that can be done

Ideas:
- Since there's cooldown, the *most common* tasks should be given the highest priority.

## Procedure

### Method 1:  Greedy Two Heap (Ready and Waiting) with Timer

Key Ideas: of all tasks that are ready, prioritize the task that has the *highest count*.  This is a *greedy* approach.

Thoughts: since the performance was so slow, there's *definitely* a faster approach.

Complexity:
- Time: each task uses heap add/pop at worst 3 times -> `O(3 * (n log n))` -> `O(n log n)`
- Space: up to `26` tasks (`"A-Z"`) in counter and heaps -> `O(1)`

### Method 2: Greedy Heap and Queue (Ready and Waiting) with Timer

Key Idea: convert the unnecessary `waiting` *heap* to a *queue*.  
- Don't need sorting in the `waiting` list; just need to get values that are ready *at all*
- Improves add/remove time complexity for `waiting` from `O(log n)` to `O(1)`

## Results (Python 3)

**Method 1**:  1417 ms, 14.3 MB (7.49%, 90.18%)

**Method 2**:  867 ms, 14.3 MB (39.82%, 90.18%)
