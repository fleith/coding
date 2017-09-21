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
        print("HashMap")
        print("size: ", self.size)
        print("array: ", self.tree)



def test_hashmap():
    hm = HashMap()
    hm['a'] = 10
    assert hm['a'] == 10