from dataclasses import dataclass, field
from typing import ClassVar

from hash_tables.hash_entry import HashEntry


@dataclass
class HashTable:
    DEFAULT_CAPACITY: ClassVar[int] = 8
    MAX_LOAD_FACTOR: ClassVar[float] = 0.75
    capacity: int = field(
        default=DEFAULT_CAPACITY,
        init=False,
    )
    buckets: list[list[HashEntry]] = field(
        default_factory=lambda: [[] for _ in range(HashTable.DEFAULT_CAPACITY)],
        init=False,
    )
    size: int = field(
        default=0,
        init=False,
    )

    @property
    def load_factor(self) -> float:
        return self.size / self.capacity

    def _should_rehash(self) -> bool:
        return self.load_factor > self.MAX_LOAD_FACTOR

    def _rehash(self) -> None:
        old_buckets = self.buckets
        self.size = 0
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        for bucket in old_buckets:
            for entry in bucket:
                self._insert_entry(entry)

    def _insert_entry(self, entry: HashEntry) -> None:
        index = self._get_bucket_index(entry.key)
        bucket = self.buckets[index]
        bucket.append(entry)
        self.size += 1

    def _get_bucket_index(self, key: int) -> int:
        return key % self.capacity

    def _get_bucket(self, key: int) -> list[HashEntry]:
        index = self._get_bucket_index(key)
        return self.buckets[index]

    def put(self, key: int, value: int) -> None:
        bucket = self._get_bucket(key)
        new_entry = HashEntry(key, value)
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
        bucket.append(new_entry)
        self.size += 1
        if self._should_rehash():
            self._rehash()

    def get(self, key: int) -> int | None:
        bucket = self._get_bucket(key)
        for entry in bucket:
            if entry.key == key:
                return entry.value
        return None

    def contains(self, key: int) -> bool:
        bucket = self._get_bucket(key)
        for entry in bucket:
            if entry.key == key:
                return True
        return False
