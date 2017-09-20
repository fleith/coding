class HashMap(object):

    def __init__(self, hash_function=hash):
        self.tree = list()
        self.hash_function = hash_function

    def __setitem__(self, key, value):
        key_list = self.tree[self.hash_function(key)]
        for index,item in enumerate(key_list):
            if item[0] == key:
                key_list[index] = key, value
                return
        key_list.append((key, value))

    def __getitem__(self, key):
        key_list = self.tree[self.hash_function(key)]
        for item in key_list:
            if item[0] == key:
                return item[1]

    def dump(self):
        print("HashMap")
        print("size: ", self.size)
        print("array: ", self.tree)



def test_hashmap():
    hm = HashMap()
    hm['a'] = 10
    assert hm['a'] == 10