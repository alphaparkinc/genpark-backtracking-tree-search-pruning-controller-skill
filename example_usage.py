from client import TreeSearchController

tsc = TreeSearchController(prune_threshold=0.5)
tsc.register_node("root", 1.0)
tsc.register_node("branch_A", 0.3, "root")
tsc.register_node("branch_B", 0.85, "root")
print("Selected Best Branch:", tsc.select_best_active_branch())
