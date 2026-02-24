from src.algorithms.sorting.heap_sort import heap_sort


def test_heap_sort_empty():
    assert heap_sort([]) == []


def test_heap_sort_single():
    assert heap_sort([1]) == [1]


def test_heap_sort_general():
    assert heap_sort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]


def test_heap_sort_duplicates():
    assert heap_sort([3, 3, 2, 1, 2]) == [1, 2, 2, 3, 3]
