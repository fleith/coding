class HashMap(object):

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
        hash_value = self.hash_function(key)
        key_list = [x[1] for x in self.tree if x[0] == hash_value]
        for item in key_list[0]:
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