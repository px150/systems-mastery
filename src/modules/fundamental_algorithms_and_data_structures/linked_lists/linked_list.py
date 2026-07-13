from dataclasses import dataclass

from .linked_list_node import LinkedListNode
from .traverse import traverse
from .remove import remove


@dataclass
class LinkedList:
    head: LinkedListNode | None = None

    def traverse(self) -> list[int]:
        return traverse(self.head)

    def remove(self, value: int) -> None:
        self.head = remove(self.head, value)
