from trees.tree_node import TreeNode


def preorder(root: TreeNode | None, result: list[int] | None = None) -> list[int]:
    if result is None:
        result = []
    if root is None:
        return result
    result.append(root.value)
    for child in root.children:
        preorder(child, result)
    return result
