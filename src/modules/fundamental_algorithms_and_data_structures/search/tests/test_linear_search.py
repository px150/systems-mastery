from search.linear_search import linear_search


def test_values_empty():
    assert linear_search([], 5) is None


def test_target_first():
    values = [5, 10, 15]
    assert linear_search(values, 5) == 0


def test_target_last():
    values = [5, 10, 15]
    assert linear_search(values, 15) == 2


def test_target_mid():
    values = [5, 10, 15]
    assert linear_search(values, 10) == 1


def test_target_absent():
    values = [5, 10, 15]
    assert linear_search(values, 20) is None


def test_target_duplicate():
    values = [5, 10, 5, 15]
    assert linear_search(values, 5) == 0
