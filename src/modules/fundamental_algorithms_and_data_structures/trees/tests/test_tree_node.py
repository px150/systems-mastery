import pytest

from trees.tree_node import TreeNode
from trees.add_child import add_child


def test_new_node_has_no_parent_and_no_children() -> None:
    node = TreeNode(value=1)

    assert node.parent is None
    assert node.children == []


def test_add_child_adds_child_to_parent():
    parent = TreeNode(value=1)
    child = TreeNode(value=2)

    add_child(parent, child)

    assert parent.children == [child]


def test_add_child_sets_parent_reference():
    parent = TreeNode(value=1)
    child = TreeNode(value=2)

    add_child(parent, child)

    assert child.parent is parent


def test_add_child_rejects_if_parent_already_exists():
    parent1 = TreeNode(value=1)
    parent2 = TreeNode(value=2)
    child = TreeNode(value=3)

    add_child(parent1, child)
    with pytest.raises(ValueError, match="Parent already exists."):
        add_child(parent2, child)


def test_add_child_rejects_when_child_is_parent():
    node = TreeNode(value=1)

    with pytest.raises(ValueError, match="Node cannot be its own child."):
        add_child(node, node)


def test_add_child_rejects_cycle() -> None:
    root = TreeNode(value=1)
    child = TreeNode(value=2)
    grandchild = TreeNode(value=3)

    add_child(root, child)
    add_child(child, grandchild)

    with pytest.raises(ValueError, match="Cycle detected."):
        add_child(grandchild, root)
