from trees.tree_node import TreeNode


def postorder(root: TreeNode | None, result: list[int] | None = None) -> list[int]:
    """
    Traverses a tree using recursive depth-first postorder traversal.

    Each node is visited after recursively exploring its children.

    Traversal state is maintained implicitly by the language call stack.
    """
    if result is None:
        result = []
    if root is None:
        return result
    for child in root.children:
        postorder(child, result)
    result.append(root.value)
    return result
