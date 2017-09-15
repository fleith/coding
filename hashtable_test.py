class HashMap(object):

    def __init__(self, size=None, hash_function=None):
        assert isinstance(size, int)
        self.array = list()
        for x in range(size):
            self.array.append(None)
        self.size = size
        self.hash_function = hash_function

    def __setitem__(self, key, value):
        self.array[hash(key) % self.size] = value

    def __getitem__(self, key):
        return self.array[hash(key) % self.size]

    def dump(self):
        for x in self.array:
            print(x)



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
    hm.dump()
