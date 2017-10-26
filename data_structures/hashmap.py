class HashMapList(object):

    def __init__(self, size=None, hash_function=hash):
        assert isinstance(size, int)
        self.array = list()
        for x in range(size):
            self.array.append(list())
        self.size = size
        self.hash_function = hash_function

    def __setitem__(self, key, value):
        key_list = self.array[self.hash_function(key) % self.size]
        for index,item in enumerate(key_list):
            if item[0] == key:
                key_list[index] = key, value
                return
        key_list.append((key, value))

    def __getitem__(self, key):
        key_list = self.array[self.hash_function(key) % self.size]
        for item in key_list:
            if item[0] == key:
                return item[1]

    def dump(self):
        print("HashMapList")
        print("size: ", self.size)
        print("array: ", self.array)



def test_HashMapList():
    hm = HashMapList(10)
    hm['a'] = 10
    assert hm['a'] == 10
    hm['a'] = 11
    assert hm['a'] == 11
    hm['b'] = 32
    assert hm['b'] == 32
    hm[2] = 3343
    assert hm[2] == 3343


def test_collision_on_HashMapList():
    hm = HashMapList(5)
    hm[0] = 0
    hm[1] = 1
    hm[2] = 2
    hm[3] = 3
    hm[4] = 4
    hm[5] = 5
    assert hm[0] == 0
    assert hm[1] == 1
    assert hm[2] == 2
    assert hm[3] == 3
    assert hm[4] == 4
    assert hm[5] == 5
    hm.dump()

def test_my_custom_hash_func():
    hm = HashMapList(5, lambda key: 1)
    hm[0] = 0
    hm[1] = 1
    hm[2] = 2
    hm[3] = 3
    hm[4] = 5
    assert hm[0] == 0
    assert hm[1] == 1
    assert hm[2] == 2
    assert hm[3] == 3
    assert hm[4] == 5
    hm.dump()

def test_my_custom_hash_func_wow():
    def my_hash_function(key):
        value = 0
        for char in str(key):
            value = value + ord(char)
        return value
    hm = HashMapList(5, my_hash_function )
    hm[0] = 0
    hm[1] = 1
    hm[2] = 2
    hm[3] = 3
    hm[4] = 5
    hm['ackd'] = 3984
    hm['b'] = 3984
    hm['a'] = 3984
    assert hm[0] == 0
    assert hm[1] == 1
    assert hm[2] == 2
    assert hm[3] == 3
    assert hm[4] == 5
    hm.dump()



class HashMapBinary(object):

    def __init__(self, hash_function=hash):
        self.tree = list()
        self.hash_function = hash_function

    def __setitem__(self, key, value):
        hash_value = self.hash_function(key)
        key_list = [x[1] for x in self.tree if x[0] == hash_value]
        if not key_list:
            key_list = list()
            self.tree.append((hash_value, key_list))
            self.tree.sort(key=lambda key: key[0])
        for index,item in enumerate(key_list):
            if item[0] == key:
                key_list[index] = key, value
                return
        key_list.append((key, value))

    def __getitem__(self, key):
        return self._getitem_binary_search(key)

    def _getitem_binary_search(self, key):
        tree_size = len(self.tree)
        if tree_size == 0:
            return None
        hash_value = self.hash_function(key)
        def binary_search(elements, value):
            if len(elements) == 0:
                return None
            slice_at = len(elements) // 2
            print(slice_at)
            if elements[slice_at][0] == value:
                return elements[slice_at][1]
            elif elements[slice_at] > value:
                return binary_search(elements[:slice_at], value)
            elif elements[slice_at] < value:
                return binary_search(elements[slice_at:], value)

        for item in binary_search(self.tree, hash_value):
            if item[0] == key:
                return item[1]



    def dump(self):
        print("HashMapBinary")
        print("size: ", self.size)
        print("array: ", self.tree)



def test_HashMapBinary():
    hm = HashMapBinary()
    hm['a'] = 10
    assert hm['a'] == 10