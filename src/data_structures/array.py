class Array:
    """Dynamic array implementation with common operations."""

    def __init__(self, capacity=10):
        """Initialize array with given capacity or from iterable."""
        if isinstance(capacity, (list, tuple)):
            self._data = list(capacity)
            self._size = len(self._data)
            self._capacity = self._size
        else:
            self._capacity = capacity
            self._data = [None] * self._capacity
            self._size = 0

    def __len__(self):
        """Return the number of elements in the array."""
        return self._size

    def __getitem__(self, index):
        """Get item at specified index."""
        if not 0 <= index < self._size:
            raise IndexError("Array index out of range")
        return self._data[index]

    def __setitem__(self, index, value):
        """Set item at specified index."""
        if not 0 <= index < self._size:
            raise IndexError("Array index out of range")
        self._data[index] = value

    def append(self, value):
        """Add an element to the end of the array."""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        """Insert an element at the specified index."""
        if not 0 <= index <= self._size:
            raise IndexError("Array index out of range")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove(self, value):
        """Remove the first occurrence of value."""
        for i in range(self._size):
            if self._data[i] == value:
                self.pop(i)
                return
        raise ValueError(f"{value} not in array")

    def pop(self, index=-1):
        """Remove and return item at index (default last)."""
        if self._size == 0:
            raise IndexError("Pop from empty array")
        if index < 0:
            index = self._size + index
        if not 0 <= index < self._size:
            raise IndexError("Array index out of range")
        value = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return value

    def index(self, value):
        """Return the index of the first occurrence of value."""
        for i in range(self._size):
            if self._data[i] == value:
                return i
        raise ValueError(f"{value} not in array")

    def _resize(self, new_capacity):
        """Resize the internal array to new_capacity."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __str__(self):
        """Return string representation of the array."""
        return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + "]"
