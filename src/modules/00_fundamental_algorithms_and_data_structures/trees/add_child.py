from trees.tree_node import TreeNode


def add_child(parent: TreeNode, child: TreeNode) -> None:
    if child is parent:
        raise ValueError("Node cannot be its own child.")
    if child.parent is not None:
        raise ValueError("Parent already exists.")
    if would_create_cycle(parent, child):
        raise ValueError("Cycle detected.")
    parent.children.append(child)
    child.parent = parent


def would_create_cycle(parent: TreeNode, child: TreeNode) -> bool:
    current_parent = parent
    while current_parent is not None:
        if current_parent == child:
            return True
        current_parent = current_parent.parent
    return False
