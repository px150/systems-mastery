from sort.selection_sort import selection_sort


def test_selection_sort_empty():
    values = []

    selection_sort(values)

    assert values == []


def test_selection_sort_single_element():
    values = [5]

    selection_sort(values)

    assert values == [5]


def test_selection_sort_unsorted():
    values = [7, 3, 9, 2, 5]

    selection_sort(values)

    assert values == [2, 3, 5, 7, 9]


def test_selection_sort_already_sorted():
    values = [2, 3, 5, 7, 9]

    selection_sort(values)

    assert values == [2, 3, 5, 7, 9]


def test_selection_sort_reverse_sorted():
    values = [9, 7, 5, 3, 2]

    selection_sort(values)

    assert values == [2, 3, 5, 7, 9]


def test_selection_sort_duplicates():
    values = [5, 2, 5, 3, 2]

    selection_sort(values)

    assert values == [2, 2, 3, 5, 5]


def test_selection_sort_negative_values():
    values = [3, -2, 0, -7, 5]

    selection_sort(values)

    assert values == [-7, -2, 0, 3, 5]
