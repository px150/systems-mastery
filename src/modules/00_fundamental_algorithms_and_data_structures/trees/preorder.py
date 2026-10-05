from trees.tree_node import TreeNode


def preorder(root: TreeNode | None, result: list[int] | None = None) -> list[int]:
    """
    Traverses a tree using recursive depth-first preorder traversal.

    Each node is visited before recursively exploring its children.

    Traversal state is maintained implicitly by the language call stack.
    """
    if result is None:
        result = []
    if root is None:
        return result
    result.append(root.value)
    for child in root.children:
        preorder(child, result)
    return result
