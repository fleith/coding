from src.algorithms.sorting.merge_sort import merge_sort


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_single():
    assert merge_sort([1]) == [1]


def test_merge_sort_general():
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]


def test_merge_sort_duplicates():
    assert merge_sort([2, 2, 1, 1, 3]) == [1, 1, 2, 2, 3]
