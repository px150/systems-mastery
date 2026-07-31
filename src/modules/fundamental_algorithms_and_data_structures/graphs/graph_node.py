from dataclasses import dataclass, field


@dataclass
class GraphNode:
    value: int
    neighbors: list["GraphNode"] = field(default_factory=list)
