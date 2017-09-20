class HashMap(object):

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
        print("HashMap")
        print("size: ", self.size)
        print("array: ", self.array)


#TODO: try to implement custom hash function
#TODO: ...
#TODO: implement hash map like a binary tree


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

def test_my_custom_hash_func():
    hm = HashMap(5, lambda key: 1)
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