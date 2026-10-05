from trees.breadth_first import breadth_first
from trees.tree_node import TreeNode
from trees.add_child import add_child


def test_breadth_first_empty_tree():
    root = None
    assert breadth_first(root) == []


def test_breadth_first_single_node_tree():
    root = TreeNode(value=1)
    assert breadth_first(root) == [1]


def test_breadth_first_tree_with_children():
    root = TreeNode(value=1)
    child1 = TreeNode(value=2)
    child2 = TreeNode(value=3)
    child3 = TreeNode(value=4)
    child4 = TreeNode(value=5)

    add_child(root, child1)
    add_child(root, child2)
    add_child(child1, child3)
    add_child(child1, child4)

    assert breadth_first(root) == [1, 2, 3, 4, 5]
