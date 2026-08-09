from dataclasses import dataclass, field

from heaps.max_heap import MaxHeap
from heaps.priority_queue.priority_item import PriorityItem


@dataclass
class PriorityQueue:
    _heap: MaxHeap = field(default_factory=MaxHeap, init=False)
    jobs: dict[int, list[str]] = field(default_factory=dict, init=False)
    items: list[PriorityItem] = field(default_factory=list)

    def __post_init__(self):
        for item in self.items:
            self.jobs.setdefault(item.priority, []).append(item.value)
        priorities = [item.priority for item in self.items]
        self._heap = MaxHeap(priorities)

    def push(self, job: str, priority: int) -> None:
        self._heap.insert(priority)
        self.jobs.setdefault(priority, []).append(job)

    def pop(self) -> str:
        priority = self._heap.peek()
        if priority is None:
            raise ValueError("There are no values in the queue.")
        values = self.jobs[priority]
        value = values.pop()
        self._heap.extract_max()
        if len(values) == 0:
            del self.jobs[priority]
        return value

    def peek(self) -> str:
        priority = self._heap.peek()
        if priority is None:
            raise ValueError("There are no values in the queue.")
        values = self.jobs[priority]
        return values[0]
