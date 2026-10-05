import pytest

from trees.tree import Tree
from trees.tree_node import TreeNode

from trees.add_child import add_child


def test_tree_owns_root() -> None:
    root = TreeNode(value=1)

    tree = Tree(root=root)

    assert tree.root is root
    assert tree.root.parent is None


def test_tree_rejects_root_with_parent() -> None:
    parent = TreeNode(value=1)
    child = TreeNode(value=2)

    add_child(parent, child)

    with pytest.raises(ValueError, match="Root can't have any parent."):
        Tree(root=child)
