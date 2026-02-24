"""Heap sort implementation."""

import heapq


def heap_sort(values):
    """Return a sorted copy of values using heap sort."""
    heap = list(values)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]
