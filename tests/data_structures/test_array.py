# tests\data_structures\test_array.py

import pytest
from src.data_structures.array import Array


def test_array_initialization_with_capacity():
    arr = Array(5)
    assert len(arr) == 0
    with pytest.raises(IndexError):
        _ = arr[0]  # Accessing empty array should raise IndexError


def test_array_initialization_with_iterable():
    arr = Array([1, 2, 3])
    assert len(arr) == 3
    assert arr[0] == 1
    assert arr[1] == 2
    assert arr[2] == 3


def test_array_append():
    arr = Array(2)
    arr.append(10)
    arr.append(20)
    assert len(arr) == 2
    assert arr[0] == 10
    assert arr[1] == 20
    arr.append(30)
    assert len(arr) == 3
    assert arr[2] == 30


def test_array_insert():
    arr = Array([1, 3, 4])
    arr.insert(1, 2)
    assert len(arr) == 4
    assert arr[0] == 1
    assert arr[1] == 2
    assert arr[2] == 3
    assert arr[3] == 4


def test_array_remove():
    arr = Array([1, 2, 3, 4])
    arr.remove(3)
    assert len(arr) == 3
    assert arr[0] == 1
    assert arr[1] == 2
    assert arr[2] == 4
    with pytest.raises(ValueError):
        arr.remove(5)  # Removing a non-existent value should raise ValueError


def test_array_pop():
    arr = Array([1, 2, 3])
    popped = arr.pop()
    assert popped == 3
    assert len(arr) == 2
    assert arr[0] == 1
    assert arr[1] == 2
    with pytest.raises(IndexError):
        Array().pop()  # Popping from an empty array should raise IndexError


def test_array_index():
    arr = Array([10, 20, 30])
    assert arr.index(20) == 1
    with pytest.raises(ValueError):
        arr.index(40)  # Accessing nonexistent element should raise ValueError


def test_array_resize():
    arr = Array(2)
    arr.append(1)
    arr.append(2)
    arr.append(3)  # This should trigger resize
    assert len(arr) == 3
    assert arr[0] == 1
    assert arr[1] == 2
    assert arr[2] == 3
