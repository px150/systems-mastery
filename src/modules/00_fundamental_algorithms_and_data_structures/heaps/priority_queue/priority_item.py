from dataclasses import dataclass


@dataclass
class PriorityItem:
    priority: int
    value: str
