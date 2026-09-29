"""Backtracking Tree Search Pruning Controller.
100% Python Standard Library.
"""

class TreeSearchController:
    """Controller scoring reasoning nodes and pruning low-value search branches."""
    def __init__(self, prune_threshold=0.4):
        self.prune_threshold = prune_threshold
        self.tree = {}

    def register_node(self, node_id: str, score: float, parent_id: str = None):
        self.tree[node_id] = {
            "score": score,
            "parent": parent_id,
            "pruned": score < self.prune_threshold,
            "children": []
        }
        if parent_id and parent_id in self.tree:
            self.tree[parent_id]["children"].append(node_id)

    def select_best_active_branch(self, leaves_only=True) -> str:
        if leaves_only:
            candidates = [nid for nid, data in self.tree.items() if not data["pruned"] and not data["children"]]
        else:
            candidates = [nid for nid, data in self.tree.items() if not data["pruned"]]
        if not candidates:
            return None
        return max(candidates, key=lambda nid: self.tree[nid]["score"])
