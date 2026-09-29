# genpark-backtracking-tree-search-pruning-controller-skill

Tree of Thoughts (ToT) backtracking controller scoring reasoning paths and pruning non-viable exploration branches.

## Architecture

```mermaid
flowchart TD
    Root[Root Thought] --> NodeA["Thought A (Score 0.2: PRUNED)"]
    Root --> NodeB["Thought B (Score 0.9: EXPLORE)"]
    NodeB --> Sub1["Thought B.1 (Score 0.85)"]
    NodeB --> Sub2["Thought B.2 (Score 0.4: PRUNED)"]
```

## Features
- **Pruning Threshold**: Cuts dead ends before resource exhaustion.
- **Pure Python**: 100% standard library.
