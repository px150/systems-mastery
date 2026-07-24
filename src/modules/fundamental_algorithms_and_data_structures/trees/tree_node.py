from dataclasses import dataclass, field


@dataclass
class TreeNode:
    value: int
    parent: "TreeNode | None" = None
    children: list["TreeNode"] = field(default_factory=list)

    def is_leaf(self) -> bool:
        return len(self.children) == 0
