import pytest

from heaps.priority_queue.priority_queue import PriorityQueue
from heaps.priority_queue.priority_item import PriorityItem


def test_push_and_pop_returns_highest_priority_value():
    queue = PriorityQueue()

    queue.push("send email", priority=50)
    queue.push("handle payment", priority=90)
    queue.push("cleanup cache", priority=20)

    assert queue.pop() == "handle payment"


def test_pop_returns_values_in_priority_order():
    queue = PriorityQueue()

    queue.push("send email", priority=50)
    queue.push("handle payment", priority=90)
    queue.push("cleanup cache", priority=20)
    queue.push("generate report", priority=70)

    assert queue.pop() == "handle payment"
    assert queue.pop() == "generate report"
    assert queue.pop() == "send email"
    assert queue.pop() == "cleanup cache"


def test_peek_returns_highest_priority_value_without_removing_it():
    queue = PriorityQueue()

    queue.push("low", priority=10)
    queue.push("high", priority=100)

    assert queue.peek() == "high"
    assert queue.peek() == "high"


def test_priority_queue_can_be_initialized_with_items():
    queue = PriorityQueue(
        [
            PriorityItem(priority=30, value="A"),
            PriorityItem(priority=90, value="B"),
            PriorityItem(priority=50, value="C"),
        ]
    )

    assert queue.pop() == "B"
    assert queue.pop() == "C"
    assert queue.pop() == "A"


def test_equal_priorities_are_all_preserved():
    queue = PriorityQueue()

    queue.push("A", priority=50)
    queue.push("B", priority=50)

    extracted = {queue.pop(), queue.pop()}

    assert extracted == {"A", "B"}


def test_pop_from_empty_queue_raises_error():
    queue = PriorityQueue()

    with pytest.raises(ValueError, match="There are no values in the queue."):
        queue.pop()


def test_equal_priorities_leave_queue_empty_after_all_values_are_popped():
    queue = PriorityQueue()

    queue.push("A", priority=50)
    queue.push("B", priority=50)

    queue.pop()
    queue.pop()

    with pytest.raises(ValueError, match="There are no values in the queue."):
        queue.pop()


def test_peek_on_empty_queue_raises_error():
    queue = PriorityQueue()

    with pytest.raises(ValueError, match="There are no values in the queue."):
        queue.peek()


def test_initialization_preserves_items_with_same_priority():
    queue = PriorityQueue(
        items=[
            PriorityItem(priority=50, value="A"),
            PriorityItem(priority=90, value="B"),
            PriorityItem(priority=50, value="C"),
        ]
    )

    assert queue.pop() == "B"

    same_priority_values = {queue.pop(), queue.pop()}

    assert same_priority_values == {"A", "C"}


def test_initialization_with_duplicate_priorities_leaves_queue_empty_after_all_pops():
    queue = PriorityQueue(
        items=[
            PriorityItem(priority=50, value="A"),
            PriorityItem(priority=90, value="B"),
            PriorityItem(priority=50, value="C"),
        ]
    )

    queue.pop()
    queue.pop()
    queue.pop()

    with pytest.raises(ValueError, match="There are no values in the queue."):
        queue.pop()
