from dataclasses import dataclass


@dataclass
class LinkedListNode:
    next: "LinkedListNode | None"
    value: int
