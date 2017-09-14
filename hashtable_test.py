class HashMap(object):
    def __init__(self):
        self.mydict = dict()
    def __setitem__(self, key, value):
        self.mydict[key] = value
    def __getitem__(self, key):
        return self.mydict[key]

myd = dict

def test_hashmap():
    hm = HashMap()
    hm['a'] = 10
    assert hm['a'] == 10
