import pytest

from stack_and_queue.stack import Stack
from arrays.dynamic_array import DynamicArray
from arrays.fixed_array import FixedArray


def create_stack() -> Stack:
    return Stack(
        _array=DynamicArray(
            array=FixedArray(
                capacity=2,
                element_size=4,
            )
        )
    )


def test_push_adds_value_to_top() -> None:
    stack = create_stack()

    stack.push(10)

    assert stack.peek() == 10


def test_peek_returns_top_without_removing_it() -> None:
    stack = create_stack()
    stack.push(10)
    stack.push(20)

    assert stack.peek() == 20
    assert stack.peek() == 20


def test_pop_removes_and_returns_top_value() -> None:
    stack = create_stack()
    stack.push(10)
    stack.push(20)

    assert stack.pop() == 20
    assert stack.peek() == 10


def test_stack_follows_lifo_order() -> None:
    stack = create_stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10


def test_push_can_trigger_underlying_array_growth() -> None:
    stack = create_stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10


def test_peek_on_empty_stack_raises_error() -> None:
    stack = create_stack()

    with pytest.raises(IndexError, match="Stack is empty."):
        stack.peek()


def test_pop_on_empty_stack_raises_error() -> None:
    stack = create_stack()

    with pytest.raises(IndexError, match="Stack is empty."):
        stack.pop()
