from dataclasses import dataclass, field
from typing import ClassVar

from hash_tables.hash_table import HashTable


@dataclass
class HashSet:
    _PRESENT: ClassVar[object] = object()
    _table: HashTable = field(default_factory=HashTable, init=False)

    @property
    def size(self) -> int:
        return self._table.size

    def contains(self, element: int) -> bool:
        return self._table.contains(element)

    def add(self, element: int) -> None:
        self._table.put(element, self._PRESENT)
