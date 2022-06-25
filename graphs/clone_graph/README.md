# Clone Graph ([LC133](https://leetcode.com/problems/clone-graph/))
Difficulty: Medium

## Problem

Given a reference of a node in a [connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph) undirected graph.

Return a [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```cpp
class Node {
    public int val;
    public List<Node> neighbors;
}
```

Constraints:
- The number of nodes in the graph is in the range `[0, 100]`.
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Empty graph (no nodes)
- Single item in graph
- Ensuring all connections are between *cloned* nodes (new `Node` instances)

Approaches:
- BFS
- DFS

## Procedure

### Method 1: Breadth First Search

Key Idea: only create connections between `Node`s that have been cloned.

Big Picture:
1. Account for empty graph by returning `None` if starting `node` is `None`
2. Create `cloned` map of `{ node.val, Node }` value, clone pairs
3. Create `nodes_to_clone` queue of `neighbors` of the original `node`
4. While there are `Nodes` in `nodes_to_clone`, get `current` `Node` and:
    - clone `Node` if not already cloned
    - create two-way connection between `current` and any of its *already cloned* neighbors
    - for any neighbor that *isn't* cloned, add it to `nodes_to_clone` to be handled later
5. Return the *clone* of the first `Node` (from the `cloned` map).

Complexity:
- Time: clone each vertex once, create bi-directional connection once -> `O(E+V)`
- Space: At most `(E+V)` edges + vertices in map and queue -> `O(E+V)`

## Results (Python 3)

**Method 1**: 78 ms, 14.4 MB (10.74%, 77.06%)
