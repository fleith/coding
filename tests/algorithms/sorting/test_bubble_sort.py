from src.algorithms.sorting.bubble_sort import bubble_sort


def test_bubble_sort_empty():
    assert bubble_sort([]) == []


def test_bubble_sort_single():
    assert bubble_sort([1]) == [1]


def test_bubble_sort_general():
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]


def test_bubble_sort_duplicates():
    assert bubble_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]
