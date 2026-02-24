import re

# Binary GAP
from collections import deque
from collections import Counter
from itertools import repeat

import sys


def solution_0(N):
    # write your code in Python 2.7
    nbin = bin(N)[-N.bit_length():]
    m = re.findall('10+(?=1)', nbin)
    return (len(max(m, key=len)) - 1) if len(m) > 0 else 0


def test_binary_gap():
    assert solution_0(66561) == 9
    assert solution_0(1162) == 3
    assert solution_0(6) == 0
    assert solution_0(328) == 2
    assert solution_0(5) == 1


# Cyclic Rotation
def solution_1(A, K):
    rotated = A
    for _ in range(K):
        last = rotated.pop()
        rotated.insert(0, last)
    return rotated


def solution_2(A, K):
    items = deque(A)
    items.rotate(K)
    return list(items)


def test_solution_1():
    assert solution_2([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution_2([-9, 0], 2) == [-9, 0]


def solution_3(A):
    for item in Counter(A).items():
        if item[1] % 2:
            return item[0]
    return None


def solution_3_b(A):
    elements = set()
    for item in A:
        if item in elements:
            elements.remove(item)
        else:
            elements.add(item)
    return elements.pop()


def test_solution_3():
    len(list([3, 4, 5]))
    assert solution_3_b([9, 3, 9, 3, 9, 7, 9]) == 7
    assert solution_3_b([9, 3, 9, 3, 9, 7, 9, 7, 7]) == 7


def frog_solution(x, y, d):
    jumps = (y - x) / d
    jumps += 1 if (y - x) % d else 0
    return jumps


def missing_number(A):
    # if len(A) == 0:
    #     return 1
    numbers = set(range(1, len(A) + 2))
    missing = numbers.difference(A)
    return missing.pop() if len(missing) > 0 else None


def test_missing_element():
    assert missing_number([1, 2, 4]) == 3
    assert missing_number([]) == 1
    assert missing_number([2]) == 1
    assert missing_number([1]) == 2


def tape_equilibrium(A):
    sum_a = A[0]
    sum_b = sum(A[1:])
    total = abs(sum_a - sum_b)
    for idx in range(1, len(A) - 1):
        sum_a += A[idx]
        sum_b -= A[idx]
        total = min(total, abs(sum_a - sum_b))
    return total


def test_tape_equilibrium():
    assert tape_equilibrium([3, 1, 2, 4, 3]) == 1
    assert tape_equilibrium([2, 100]) == 98
    assert tape_equilibrium([-1000, 1000]) == 2000
    assert tape_equilibrium([2, 100]) == 98
    assert tape_equilibrium([2, 100]) == 98


def equilibrium(A):
    left = 0
    right = sum(A)
    for idx, ele in enumerate(A):
        right -= ele
        if left == right:
            return idx
        left += ele

    if left == right:
        return len(A) - 1
    return -1


def test_equilibrium():
    assert equilibrium([1, 2, 1]) == 1
    assert equilibrium([1082132608, 0, 1082132608]) == 1
    assert equilibrium([2, 1, 2]) == 1
    assert equilibrium([0, 2147483647, 2147483647, 2147483647]) == 2
    assert equilibrium([2, -1, -2, 1, 500]) == 4
    assert equilibrium([1, 2, -3, 0]) == 3
    assert equilibrium([0, -1]) == 1
    assert equilibrium([0, 1]) == 1
    assert equilibrium([-1, 0, -1]) == 1
    assert equilibrium([-1, 1, 0]) == 2
    # assert equilibrium([0]) == -1
    # assert equilibrium([]) == -1


#
# def solution(A):
#     # write your code in Python 2.7
#     indexes_by_element = {}
#     result = 0
#     for element in A:
#         if element in indexes_by_element:
#             result += indexes_by_element[element]
#             if result > 1000000000:
#                 return 1000000000
#             indexes_by_element[element] += 1
#         else:
#             indexes_by_element[element] = 1
#
#     return result
#
# def test_solution():
#     assert solution([3, 5, 6, 3, 3, 5]) == 4
#     assert solution([3, 5, 6, 3, 3, 5, 3, 5, 6, 3, 3, 5]) == 22
#     assert solution([3, 3]) == 1
#     assert solution([3]) == 0
#     assert solution([]) == 0
#     assert solution(repeat(1,900000000000000000)) == 1000000000

def color_next_row(idx_row, idx_column, A):
    try:
        return A[idx_row + 1][idx_column]
    except IndexError:
        return None


def color_next_column(idx_row, idx_column, A):
    try:
        return A[idx_row][idx_column + 1]
    except IndexError:
        return None


def next_column_was_processed(idx_row, idx_column, processed):
    if (idx_row, idx_column + 1) in processed:
        return True
    processed.add((idx_row, idx_column + 1))
    return False


def next_row_was_processed(idx_row, idx_column, processed):
    if (idx_row + 1, idx_column) in processed:
        return True
    processed.add((idx_row + 1, idx_column))
    return False


def solution(A):
    # write your code in Python 2.7
    total_countries = 0
    processed = set()
    for idx_row, row in enumerate(A):
        for idx_column, color in enumerate(row):
            color_processed = False
            if (idx_row, idx_column) in processed:
                color_processed = True
            processed.add((idx_row, idx_column))

            if color == color_next_row(idx_row, idx_column, A):
                if next_row_was_processed(idx_row, idx_column, processed):
                    color_processed = True

            if color == color_next_column(idx_row, idx_column, A):
                if next_column_was_processed(idx_row, idx_column, processed):
                    color_processed = True

            if not color_processed:
                total_countries += 1

    return total_countries


def test_solution():
    assert solution([[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]) == 11
    # assert solution([3, 5, 6, 3, 3, 5, 3, 5, 6, 3, 3, 5]) == 22
    # assert solution([3, 3]) == 1

