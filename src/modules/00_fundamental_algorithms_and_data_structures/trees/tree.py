from dataclasses import dataclass

from trees.tree_node import TreeNode


@dataclass
class Tree:
    root: TreeNode

    def __post_init__(self) -> None:
        if self.root.parent is not None:
            raise ValueError("Root can't have any parent.")
