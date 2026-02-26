from src.algorithms.sorting.quick_sort import quick_sort
import random

def test_quick_sort_empty():
    assert quick_sort([]) == []


def test_quick_sort_single():
    assert quick_sort([1]) == [1]


def test_quick_sort_general():
    assert quick_sort([10, -1, 2, 5, 0, 6, 4, -5]) == [-5, -1, 0, 2, 4, 5, 6, 10]


def test_quick_sort_duplicates():
    assert quick_sort([4, 2, 4, 1, 4]) == [1, 2, 4, 4, 4]


def test_quick_sort_long_list():
    nums = [random.randint(0, 100000) for _ in range(10000)]
    assert quick_sort(nums) == sorted(nums)

