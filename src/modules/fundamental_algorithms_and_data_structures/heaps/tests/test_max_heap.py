from heaps.max_heap import MaxHeap


def test_insert_into_empty_heap():
    heap = MaxHeap()

    heap.insert(10)

    assert heap.values == [10]


def test_insert_sifts_larger_value_up():
    heap = MaxHeap()

    heap.insert(10)
    heap.insert(20)

    assert heap.values == [20, 10]


def test_insert_sifts_value_up_multiple_levels():
    heap = MaxHeap()

    for value in [50, 30, 40, 10, 20, 35, 60]:
        heap.insert(value)

    assert heap.values == [60, 30, 50, 10, 20, 35, 40]


def test_peek_returns_max_value():
    heap = MaxHeap()

    for value in [50, 30, 40, 10, 20, 35, 60]:
        heap.insert(value)

    assert heap.peek() == 60


def test_peek_does_not_remove_value():
    heap = MaxHeap()
    heap.insert(10)

    heap.peek()

    assert heap.values == [10]


def test_extract_max_removes_and_returns_single_value():
    heap = MaxHeap()
    heap.insert(10)

    result = heap.extract_max()

    assert result == 10
    assert heap.values == []


def test_extract_max_sifts_replacement_down_multiple_levels():
    heap = MaxHeap()

    for value in [100, 80, 90, 70, 60, 50, 40]:
        heap.insert(value)

    result = heap.extract_max()

    assert result == 100
    assert heap.values == [90, 80, 50, 70, 60, 40]


def test_extract_max_sifts_down_when_node_has_only_left_child():
    heap = MaxHeap()

    for value in [100, 80, 90, 70, 60, 50]:
        heap.insert(value)

    result = heap.extract_max()

    assert result == 100
    assert heap.values == [90, 80, 50, 70, 60]


def test_extract_max_returns_all_values_in_descending_order():
    heap = MaxHeap()

    for value in [40, 10, 70, 30, 90, 20, 60]:
        heap.insert(value)

    extracted = []

    while heap.peek() is not None:
        extracted.append(heap.extract_max())

    assert extracted == [90, 70, 60, 40, 30, 20, 10]
    assert heap.values == []


def test_initial_values_are_heapified():
    heap = MaxHeap([12, 50, 3, 90, 40, 70, 20])

    assert heap.values == [90, 50, 70, 12, 40, 3, 20]


def test_initial_values_are_not_modified():
    values = [12, 50, 3, 90, 40, 70, 20]

    MaxHeap(values)

    assert values == [12, 50, 3, 90, 40, 70, 20]
