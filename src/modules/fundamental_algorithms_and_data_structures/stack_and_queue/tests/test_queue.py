import pytest

from arrays.dynamic_array import DynamicArray
from arrays.fixed_array import FixedArray
from stack_and_queue.queue import Queue


def create_queue() -> Queue:
    return Queue(
        _array=DynamicArray(
            array=FixedArray(
                capacity=2,
                element_size=4,
            )
        )
    )


def test_enqueue_adds_value_to_back() -> None:
    queue = create_queue()

    queue.enqueue(10)

    assert queue.peek() == 10


def test_peek_returns_front_without_removing_it() -> None:
    queue = create_queue()
    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.peek() == 10
    assert queue.peek() == 10


def test_dequeue_returns_front_and_removes_it() -> None:
    queue = create_queue()
    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.dequeue() == 10
    assert queue.peek() == 20


def test_queue_follows_fifo_order() -> None:
    queue = create_queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30


def test_enqueue_can_trigger_underlying_array_growth() -> None:
    queue = create_queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30


def test_peek_on_empty_queue_raises_error() -> None:
    queue = create_queue()

    with pytest.raises(IndexError, match="Queue is empty."):
        queue.peek()


def test_dequeue_on_empty_queue_raises_error() -> None:
    queue = create_queue()

    with pytest.raises(IndexError, match="Queue is empty."):
        queue.dequeue()
