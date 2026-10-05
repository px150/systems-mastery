from trees.tree_node import TreeNode


def preorder_iterative(root: TreeNode | None) -> list[int]:
    """
    Traverses a tree using iterative depth-first preorder traversal.

    Each node is visited before its children.

    Traversal state is maintained explicitly using a stack instead of
    the language call stack.
    """
    result = []
    if root is None:
        return result
    stack = [root]
    while stack:
        current = stack.pop()
        result.append(current.value)
        for child in reversed(current.children):
            stack.append(child)
    return result
