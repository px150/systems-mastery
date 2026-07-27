from collections import deque

from trees.tree_node import TreeNode


def breadth_first(root: TreeNode | None) -> list[int]:
    """
    Traverses a tree using breadth-first traversal.

    Nodes are visited level by level, from the root toward deeper levels.

    Traversal state is maintained explicitly using a queue.
    """
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.value)
        for child in current.children:
            queue.append(child)
    return result
