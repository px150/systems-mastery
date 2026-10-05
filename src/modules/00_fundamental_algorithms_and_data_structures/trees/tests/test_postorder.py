from trees.postorder import postorder
from trees.tree_node import TreeNode
from trees.add_child import add_child


def test_postorder_empty_tree():
    root = None
    assert postorder(root) == []


def test_postorder_single_node_tree():
    root = TreeNode(value=1)
    assert postorder(root) == [1]


def test_postorder_tree_with_children():
    root = TreeNode(value=1)
    child1 = TreeNode(value=2)
    child2 = TreeNode(value=3)
    child3 = TreeNode(value=4)
    child4 = TreeNode(value=5)

    add_child(root, child1)
    add_child(root, child2)
    add_child(child1, child3)
    add_child(child1, child4)

    assert postorder(root) == [4, 5, 2, 3, 1]
