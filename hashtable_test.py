class HashMap(object):

    def __init__(self, size=None, hash_function=None):
        assert isinstance(size, int)
        self.array = list()
        for x in range(size):
            self.array.append(dict())
        self.size = size
        self.hash_function = hash_function

    def __setitem__(self, key, value):
        key_map = self.array[hash(key) % self.size]
        key_map[key] = value

    def __getitem__(self, key):
        key_map = self.array[hash(key) % self.size]
        return key_map[key]

    def dump(self):
        print("HashMap")
        print("size: ", self.size)
        print("array: ", self.array)



def test_hashmap():
    hm = HashMap(10)
    hm['a'] = 10
    assert hm['a'] == 10
    hm['a'] = 11
    assert hm['a'] == 11
    hm['b'] = 32
    assert hm['b'] == 32
    hm[2] = 3343
    assert hm[2] == 3343


def test_collision_on_hashmap():
    hm = HashMap(5)
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