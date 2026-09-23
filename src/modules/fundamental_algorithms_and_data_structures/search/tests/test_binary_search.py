from search.binary_search import binary_search


def test_values_empty():
    assert binary_search([], 5) is None


def test_single_value_target_first():
    sorted_values = [5]
    assert binary_search(sorted_values, 5) == 0


def test_single_value_target_absent():
    sorted_values = [5]
    assert binary_search(sorted_values, 10) is None


def test_values_even():
    sorted_values = [5, 10, 15, 20]
    assert binary_search(sorted_values, 15) == 2


def test_values_odd():
    sorted_values = [5, 10, 15, 20, 25]
    assert binary_search(sorted_values, 15) == 2


def test_values_most_left():
    sorted_values = [5, 10, 15, 20, 25]
    assert binary_search(sorted_values, 5) == 0


def test_values_most_right():
    sorted_values = [5, 10, 15, 20, 25]
    assert binary_search(sorted_values, 25) == 4


def test_target_absent():
    sorted_values = [5, 10, 15, 20, 25]
    assert binary_search(sorted_values, 17) is None


def test_target_requires_repeated_left_search():
    sorted_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(sorted_values, 1) == 0


def test_target_requires_repeated_right_search():
    sorted_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(sorted_values, 10) == 9
